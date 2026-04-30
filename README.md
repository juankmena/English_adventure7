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
