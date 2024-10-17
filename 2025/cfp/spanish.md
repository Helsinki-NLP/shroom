**Si tienes mucha prisa (TL;DR)**  
[*Mu-SHROOM*](https://helsinki-nlp.github.io/shroom/) *es una tarea compartida (Shared Task) de SemEval 2025\. Nuestro objetivo es impulsar la investigación en detección de alucinaciones para contenido generado con LLMs (Large Language Model, por sus siglas en inglés). Hemos anotado contenido alucinado en 10 idiomas diferentes generado por modelos de lenguaje de última generación. Puedes participar en tantos idiomas como desees, identificando con precisión las secciones de contenido alucinado en nuestros datos de prueba. La tarea consiste en identificar con precisión las secciones o fragmentos del texto que son alucinados. ¡Mantente informado suscribiéndote a nuestro [Google group](https://groups.google.com/g/semeval-2025-task-3-mu-shroom) y/o al [Slack](https://join.slack.com/t/shroom-shared-task/shared_invite/zt-2mmn4i8h2-HvRBdK5f4550YHydj5lpnA)\!*

**Invitación completa**  
Nos es grato anunciar Mu-SHROOM, una shared task para mejorar los métodos para detección de alucinaciones ([visita nuestra página](https://helsinki-nlp.github.io/shroom/)). Invitamos a los participantes a detectar los fragmentos del texto que son alucinaciones en textos generados con LLMs (Large Language Model, por sus siglas en inglés) multilingües de última generación. 

**Introducción**  
Hemos diseñado Mu-SHROOM a partir de lo lo aprendido en la primera iteración de nuestra shared task en alucinaciones: [SHROOM](https://helsinki-nlp.github.io/shroom/2024). En Mu-SHROOM incorporamos tres mejoras fundamentales: 1\) un enfoque en modelos de lenguaje grandes (LLM), 2\) anotaciones multilingües en 10 idiomas y 3\) la tarea ahora consiste en predecir los fragmentos del texto que son alucinaciones. 

Los LLM con frecuencia producen “alucinaciones”, es decir,  generan texto plausible pero incorrecto. Además, las métricas de evaluación actuales priorizan la fluidez del texto por encima de cuán correcto es. Esto da lugar a un problema cada vez más preocupante a medida que estos modelos son adoptados más ampliamente por el público. 

Con Mu-SHROOM, queremos promover el desarrollo de métodos para la detección de contenidos alucinados. Esta nueva iteración de la tarea compartida se desarrolla en un contexto multilingüe y multimodelo. En otras palabras, proporcionamos datos producidos por una variedad de LLMs abiertos en 10 idiomas diferentes (alemán, árabe (estándar moderno), chino (mandarín), español, finés, francés, hindi, inglés, italiano y sueco).

Invitamos a grupos de investigación a participar en cualquiera de los idiomas disponibles. Para participar deben desarrollar sistemas capaces de identificar y mitigar con precisión las alucinaciones en contenidos generados por LLMs.   
Como es habitual en SemEval, se invitará a los participantes a que envíen artículos de investigación con la descripción de sus sistemas, con la opción de presentarlos el próximo taller SemEval 2025 (que coincidirá con una de las próximas conferencias \*ACL). Los participantes que opten por escribir un artículo de descripción del sistema deberán también participar en procesos de revisión de artículos (máximo 2 artículos por autor).

**Fechas clave:**  
Todas las fechas indicadas son “en cualquier lugar del mundo” (i.e., 23:59 UTC-12).

* Publicacion del Dev set: 02.09.2024  
* Publicación del Test set: 01.01.2025  
* Fin de la fase de evaluación: 31.01.2025  
* Enviar artículos de descripción del sistema: 28.02.2025 (por confirmar)  
* Notificación de aceptación: 31.03.2025 (por confirmar)  
* Versión final editada: 21.04.2025 (por confirmar)  
* Taller SemEval: Verano de 2025 (en una conferencia de la ACL)

**Métricas de evaluación:**   
Usaremos dos métricas:

1. IoU (intersection-over-union, en inglés): la intersección de los caracteres marcados como alucinaciones en la referencia anotada sobre aquellos caracteres predichos como alucinaciones  
2. la correlación entre la probabilidad asignada de que un carácter forme parte de una alucinación y las probabilidades empíricas observadas en nuestras anotaciones.

Las clasificaciones serán realizadas independientemente por idioma: es posible participar en los idiomas que les interesen\!

**¿Cómo participar?**

* registrarse: registre a su equipo antes de enviar su trabajo en [https://mushroomeval.pythonanywhere.com](https://mushroomeval.pythonanywhere.com)  
* Envío de resultados: a través de nuestra plataforma se puede enviar resultados antes del 31 de enero de 2025  
* Artículo de investigación con la descripción del sistema: los artículos deben enviarse antes del 28 de febrero de 2025 (por confirmar).

**¿Quieres mantenerte al tanto?**  
Puedes suscribirte a nuestro [Google group](https://groups.google.com/g/semeval-2025-task-3-mu-shroom) o también al [Slack](https://join.slack.com/t/shroom-shared-task/shared_invite/zt-2mmn4i8h2-HvRBdK5f4550YHydj5lpnA) que hemos creado\! 

Esperamos contar con su/vuestra participación.

Saludos,  
Raúl Vázquez y Timothee Mickus   
En nombre de todos los organizadores de Mu-SHROOM

