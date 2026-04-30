# English Adventure 7th Grade - Streamlit FULL ADMIN

App independiente de práctica para inglés de 7th grade, basada en los topics y prácticas proporcionadas.

## Usuario administrador por defecto

- Usuario: `admin`
- Contraseña: `admin123`

Recomendación: entra con ese usuario y cambia la contraseña desde **Admin Panel > Users > Change password**.

## Funciones incluidas

- Login y registro de estudiantes.
- Usuario administrador.
- Panel de administrador.
- Creación de usuarios desde admin.
- Cambio de contraseña.
- Cambio de rol: student/admin.
- Eliminación de usuarios.
- Reinicio de progreso por usuario.
- Estadísticas globales.
- Estadísticas por usuario.
- Estadísticas por mundo/tema.
- Revisión de intentos recientes.
- Exportación CSV del progreso.
- Exportación JSON de progreso.
- Exportación JSON de usuarios sin contraseñas.
- Study cards con audio usando voz del navegador.
- Writing Lab con validación básica.
- Reading Challenge.
- Idioms.

## Cómo ejecutar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Cómo subir a Streamlit Cloud

1. Sube esta carpeta a un repositorio de GitHub.
2. En Streamlit Cloud crea una nueva app.
3. Selecciona el archivo principal: `app.py`.
4. Deploy.

## Notas importantes

- Los usuarios y progreso se guardan en archivos JSON dentro de `storage/`.
- Las contraseñas se guardan como hash SHA-256, no como texto plano.
- En Streamlit Cloud los archivos JSON pueden reiniciarse si se redeploya la app o si el entorno se reinicia. Para uso permanente se puede migrar a SQLite, Google Sheets o Supabase.
- Los audios usan `speechSynthesis` del navegador; no requiere MP3 ni servicios externos.


## Versión PRO

Esta versión incorpora:

1. Vidas/corazones por práctica.
2. Badges/insignias automáticas.
3. Ranking de usuarios.
4. Rachas diarias.
5. Misiones diarias.
6. Modo adaptativo con áreas débiles.
7. Banco de errores.
8. Botón/sección Practice My Weak Areas.
9. Examen simulado.
10. Writing Lab mejorado.
11. Reading Detective.
12. Flashcards / Study Cards.
13. Grammar Map.
14. Dashboard admin ampliado.
15. Exportación CSV, JSON y Excel.
16. Mascota gato fija y feedback visual.
17. Pantalla/efectos de logro con confetti, globos y sonido.
18. SQLite para respaldo de intentos y analítica, además de almacenamiento JSON compatible.

## Cambio de contraseña

Ruta para cualquier usuario:
`Sidebar > My Profile > Change my password`

Ruta de administrador:
`Sidebar > Admin Panel > Users > Manage existing user > Change password`

## Usuario administrador por defecto

- Usuario: `admin`
- Contraseña: `admin123`

Se recomienda cambiar la contraseña al primer ingreso.

## Ejecutar

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Update: Word Bank en Vocabulary

Esta versión incorpora Word Bank en:

- Vocabulary Unit 1: banco general de palabras.
- Vocabulary Unit 2: banco general y banco clasificado por Verbs, Places, Nouns y Adjectives / other words.
- Writing Lab: banco de apoyo cuando la tarea corresponde a Unit 2 o Idioms.

También incluye modo de práctica tipo examen ocultando el Word Bank:

- Vocabulary Unit 1 > Word Bank mode > Hide word bank / exam practice
- Vocabulary Unit 2 > Word Bank mode > Hide word bank / exam practice


## Voice Settings / Test Voice

La app incluye una sección:

```text
Sidebar > Voice Settings
```

Use esa pantalla para probar si el dispositivo está usando una voz inglesa.

En iPad, si se escucha como hispanohablante leyendo inglés, active o descargue una voz inglesa:

```text
Settings > Accessibility > Spoken Content > Voices > English
```

Recomendadas: Samantha, Alex, Google US English, Google UK English o Microsoft English voices.
