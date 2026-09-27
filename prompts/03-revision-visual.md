# Prompt 3 · Que la IA revise su propia web antes de publicar

Para asistentes que pueden ejecutar código (Claude Code, Cursor, etc.).

```
Antes de publicar, levanta la web en local y revísala como lo haría un usuario:
1. Abre la página a 1360 px y a 400 px de ancho (móvil) con Playwright.
2. Haz una captura de página completa de cada una y míralas.
3. Comprueba: errores de JavaScript en consola, desbordamiento horizontal en móvil
   (document.documentElement.scrollWidth debe ser igual al ancho), textos cortados,
   números sin separador de miles, mapas o gráficos vacíos, enlaces rotos.
4. Compara 3 cifras de la web con el fichero de datos y con la fuente original.
5. Haz una sola ronda de correcciones y dime qué has cambiado.
```

En Techo, esta revisión encontró antes de publicar: el proveedor del mapa exigía una clave nueva, las cifras de 4 dígitos salían sin punto de miles y la página se desbordaba en el móvil.
