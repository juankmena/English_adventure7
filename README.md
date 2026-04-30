# English Adventure 7th Grade - Streamlit

App independiente de práctica para inglés de 7th grade, basada en los topics y prácticas proporcionadas.

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

## Notas

- Los usuarios y progreso se guardan en archivos JSON dentro de `storage/`.
- En Streamlit Cloud esos archivos pueden reiniciarse si la app se redeploya. Para uso permanente se puede migrar a SQLite o Google Sheets.
- Los audios usan la voz del navegador con `speechSynthesis`, por lo que no necesita archivos MP3 ni servicios externos.
