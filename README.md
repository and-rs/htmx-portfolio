### AI Categorizer

1. Install uv (please install globally)
   ```
   pip install uv
   ```

2. install dependencies
   ```
   uv sync
   ```

3. Start the app locally
   ```
   uv run fastapi dev
   ```

4. Start the TailwindCSS CLI to update css in realtime
   ```
   uv run tailwind.py
   ```

### TODO (project optimization)

- [ ] download fonts
- [ ] gzip and compress html and css files (htmx)
- [ ] html image component
- [ ] script for image compression and resizin
- [ ] script for updating static dependencies
- [ ] black, djlint and basedpyright pre-commit pipeline
- [ ] integrate rustywind?
- [x] rethink basecoat usage and treeshake the css and js
- [x] jinja fragments (not necessary)
- [x] fix hot-reload types (arel)
- [x] autoreload tailwind stylesheet
