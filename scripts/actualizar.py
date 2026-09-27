#!/usr/bin/env python3
"""Descarga el dato de ejemplo y genera site/data.json.

Ejemplo incluido: coste salarial por trabajador y mes, por comunidad autónoma
(INE, Encuesta Trimestral de Coste Laboral, tabla 6061). No necesita clave.

Para tu proyecto: cambia FUENTE y la función transformar(). Mantén siempre
la fuente, el periodo y la fecha de descarga junto al dato.
"""
from __future__ import annotations

import json
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FUENTE = {
    "nombre": "INE, Encuesta Trimestral de Coste Laboral (tabla 6061)",
    "url_api": "https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/6061?nult=5",
    "url_web": "https://www.ine.es/jaxiT3/Tabla.htm?t=6061",
    "licencia": "Reutilización libre citando la fuente (INE)",
}
# Nombre del INE -> código de comunidad autónoma
CCAA = {"Andalucía": "01", "Aragón": "02", "Asturias, Principado de": "03", "Balears, Illes": "04", "Canarias": "05",
        "Cantabria": "06", "Castilla y León": "07", "Castilla - La Mancha": "08", "Cataluña": "09",
        "Comunitat Valenciana": "10", "Extremadura": "11", "Galicia": "12", "Madrid, Comunidad de": "13",
        "Murcia, Región de": "14", "Navarra, Comunidad Foral de": "15", "País Vasco": "16", "Rioja, La": "17"}


def descargar(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "observatorio-datos-plantilla/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def transformar(series):
    """Convierte la respuesta del INE en {codigo: {nombre, valor, variacion}}."""
    out, periodo = {}, None
    for s in series:
        nombre = s["Nombre"]
        if "Industria, construcción y servicios" not in nombre or "Coste salarial total" not in nombre:
            continue
        region = nombre.split(". ")[0]
        puntos = {(x["Anyo"], x["FK_Periodo"]): x["Valor"] for x in s["Data"]}
        if not puntos:
            continue
        y, p = max(puntos)
        previo = puntos.get((y - 1, p))
        periodo = f"{p - 18}T {y}" if 19 <= p <= 22 else str(y)
        dato = {"valor": round(puntos[(y, p)], 2),
                "variacion": round((puntos[(y, p)] / previo - 1) * 100, 1) if previo else None}
        if region == "Total Nacional":
            out["ES"] = {"nombre": "España", **dato}
        elif region in CCAA:
            out[CCAA[region]] = {"nombre": region, **dato}
    return out, periodo


def validar(datos) -> None:
    """Reglas mínimas: si fallan, no se publica nada (mejor datos de ayer que datos rotos)."""
    faltan = set(CCAA.values()) - set(datos)
    if faltan:
        raise SystemExit(f"Faltan comunidades: {sorted(faltan)}")
    for c, d in datos.items():
        if not 500 < d["valor"] < 10000:
            raise SystemExit(f"Valor imposible en {c}: {d['valor']}")


def main() -> int:
    datos, periodo = transformar(descargar(FUENTE["url_api"]))
    validar(datos)
    salida = {
        "titulo": "Coste salarial por trabajador y mes",
        "unidad": "€/mes",
        "periodo": periodo,
        "descargado": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "fuente": FUENTE,
        "datos": datos,
    }
    (ROOT / "site" / "data.json").write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"OK {periodo}: España {datos['ES']['valor']} €/mes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
