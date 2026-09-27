# Prompt 2 · Verificar y limpiar antes de publicar

```
Revisa este conjunto de datos antes de publicarlo: [PEGA O ADJUNTA EL JSON].

Comprueba:
1. Totales: ¿la suma de las partes cuadra con el total? ¿Hay territorios contados dos veces?
2. Valores imposibles: negativos, ceros sospechosos, órdenes de magnitud raros
   (por ejemplo, un importe 20 veces mayor que su presupuesto).
3. Coherencia temporal: saltos bruscos entre periodos; ¿hay un cambio de metodología que lo explique?
4. Unidades: €/m² frente a € totales, con o sin IVA, mensual frente a anual, tasa por 100.000 habitantes.
5. Comparabilidad: ¿estoy mezclando fuentes que miden cosas distintas (por ejemplo, tasación frente a precio de anuncio)?
6. Cada cifra que voy a destacar en un titular: ¿coincide con la fuente original? Dame el enlace exacto.

Devuélveme una tabla con: problema, filas afectadas, gravedad (alta/media/baja) y corrección propuesta.
No corrijas nada sin decírmelo.
```

Trampas reales encontradas en Techo y Oferta Única:
- El CGPJ publica Ceuta y Melilla dentro de Andalucía: sumarlos aparte es contar dos veces.
- La nota de prensa decía 25.540 desahucios; el Excel oficial, 24.540.
- Casi 5.000 contratos con importes imposibles (un transporte de 22.000 € «adjudicado» por 1.954 M€).
- Los acuerdos marco repiten el importe total en cada adjudicatario: hay que dividir.
- Varios órganos de un mismo ayuntamiento comparten código: identifícalos también por su nombre.
