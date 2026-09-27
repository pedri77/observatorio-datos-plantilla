# Prompt 1 · Investigar datos con un agente que no inventa

Úsalo con cualquier asistente con búsqueda web (Claude, ChatGPT, Gemini). Lanza un agente por tema, en paralelo.

```
Hoy es [FECHA]. Investiga datos REALES y verificables sobre [TEMA] en [TERRITORIO].
Fuente preferente: [ORGANISMO OFICIAL, p. ej. INE, CGPJ, Ministerio X, portal autonómico].

Necesito:
1. [DATO 1] por [UNIDAD TERRITORIAL] para los años [RANGO].
2. [DATO 2] ...
3. Contexto normativo relevante (leyes o decretos con su enlace al boletín oficial).

Reglas obligatorias:
- Cada cifra con su fuente: nombre, enlace comprobable y periodo al que se refiere.
- Si no encuentras un dato en una fuente fiable, déjalo vacío (null). NUNCA lo inventes ni lo estimes sin decirlo.
- Si dos fuentes no coinciden, dame las dos y explica la diferencia.
- Indica las trampas de los datos (doble conteo, cambios de metodología, unidades, IVA incluido o no).

Salida: un fichero JSON con esta estructura:
{"datos": [{"territorio", "codigo", "periodo", "valor", "unidad", "fuente_url"}], "notas": [], "fuentes": [{"nombre", "url", "consultado"}]}
Al final, un resumen breve de cobertura, confianza y huecos.
```

**Por qué funciona:** la frase «déjalo vacío, nunca lo inventes» cambia el comportamiento del modelo. Sin ella, rellena huecos con cifras plausibles.
