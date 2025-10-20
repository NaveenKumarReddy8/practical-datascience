mkdir docs

files=("chapter_1_eda.py")

for file in "${files[@]}"; do
  without_extension="${file%.*}"
  uv run marimo export html-wasm "$file" -o docs/"$without_extension".html --mode run
done

echo "<html><body><ul>" > docs/index.html
for file in "${files[@]}"; do
  without_extension="${file%.*}"
  echo "<li><a href=\"$without_extension.html\">$without_extension</a></li>" >> docs/index.html
done
echo "</ul></body></html>" >> docs/index.html