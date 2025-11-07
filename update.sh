#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
VIEW_DIR="$SCRIPT_DIR/src/app/views"

cd "$VIEW_DIR"

echo "Compilando arquivos .ui..."

for ui_file in ui_files/*.ui; do
    base_name=$(basename "$ui_file" .ui)
    
    final_name=${base_name/_screen/}
    
    output_file="ui_${final_name}.py"
    
    echo "  $ui_file -> $output_file"
    pyside6-uic "$ui_file" -o "$output_file"
done

echo "Concluído."