# Implementación de un Sistema de Gestión de Vehículos

La empresa AutoTech necesita un sistema para gestionar diferentes tipos de vehículos. Cada vehículo tiene atributos comunes como marca, modelo y año, pero también atributos específicos según su tipo (coche, motocicleta, camión). El sistema debe permitir la creación de vehículos, la consulta de sus atributos y la realización de acciones específicas para cada tipo de vehículo.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Programación Orientada a Objetos |
| **Nivel** | junior-l1 |
| **Tipo** | practical |
| **Tiempo estimado** | 3-4 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Definición de la Jerarquía de Vehículos

**Objetivo:** Crear una jerarquía de clases que represente la relación entre los diferentes tipos de vehículos.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Identificar los atributos comunes y específicos de cada tipo de vehículo.
- Aplicar los principios de herencia y abstracción para crear la jerarquía de clases.

**Entregable:** Jerarquía de clases implementada.

<details>
<summary>Pistas de conocimiento</summary>

- Recuerda que la herencia permite compartir atributos y métodos entre clases.
- La abstracción te ayuda a ocultar detalles de implementación y exponer solo lo necesario.

</details>

### Fase 2: Implementación de Métodos Específicos

**Objetivo:** Agregar métodos específicos a cada tipo de vehículo que realicen acciones relacionadas con su tipo.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Identificar acciones específicas para cada tipo de vehículo.
- Implementar métodos en cada clase que realicen estas acciones, aplicando el principio de polimorfismo.

**Entregable:** Métodos específicos implementados en cada clase de vehículo.

<details>
<summary>Pistas de conocimiento</summary>

- El polimorfismo te permite utilizar un mismo nombre de método para acciones diferentes según el tipo de objeto.
- Asegúrate de que los métodos sean coherentes con las acciones que deben realizar.

</details>

### Fase 3: Gestión de Vehículos

**Objetivo:** Crear un sistema que permita la gestión de vehículos, incluyendo la creación, consulta y realización de acciones específicas.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Implementar un sistema que permita crear instancias de vehículos y realizar acciones específicas.
- Asegurar que el sistema respete el encapsulamiento al manejar los atributos de los vehículos.

**Entregable:** Sistema de gestión de vehículos funcional.

<details>
<summary>Pistas de conocimiento</summary>

- El encapsulamiento te ayuda a proteger los datos de los vehículos y controlar su acceso.
- Asegúrate de que los métodos de creación y consulta de vehículos respeten el encapsulamiento.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es la herencia en el contexto de este reto?
- **paraQueSirve**: ¿Para qué sirve el polimorfismo en este sistema de gestión de vehículos?
- **comoSeUsa**: ¿Cómo se usa el encapsulamiento para proteger los datos de los vehículos?
- **erroresComunes**: ¿Qué error común podrías cometer al implementar la jerarquía de clases?

## Criterios de Evaluacion

- Implementar una jerarquía de clases que represente la relación entre diferentes tipos de vehículos.
- Agregar métodos específicos a cada tipo de vehículo que realicen acciones relacionadas con su tipo.
- Crear un sistema que permita la gestión de vehículos, incluyendo la creación, consulta y realización de acciones específicas.

---

*Reto generado automaticamente por Challenge Generator - Pragma*
