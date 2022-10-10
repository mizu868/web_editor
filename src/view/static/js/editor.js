// ace.editor()で、Editorオブジェクトを返す
let editor = ace.edit("editor");
// Editorオブジェクトにエディタのモードを割り当てる
editor.getSession().setMode("ace/mode/python");
editor.setTheme("ace/theme/monokai");
editor.setOptions({
    enableBasicAutocompletion: true,
    enableSnippets: true,
    enableLiveAutocompletion: true
});
editor.setValue("# Let's coding here python!\n", 1);

const javaMainSrc = "import java.util.*;\n\
 \n\
public class Main {\n \
    public static void main(String[] args) throws Exception {\n \
        // Your code here!\n \
        System.out.println(\"hello java!\");\n \
    }\n \
}\n";

function selectLang(){
    var selectValue = document.getElementById("langs").value;
    if(selectValue == 'python'){
        editor.getSession().setMode("ace/mode/python");
        editor.setValue("# Let's coding here python!\n", 1);
        //document.getElementById("result_text").value = '';
    }else if(selectValue == 'java'){
        editor.getSession().setMode("ace/mode/java");
        editor.setValue(javaMainSrc, 1);
        //document.getElementById("result_text").value = '';
    }
}

window.addEventListener('DOMContentLoaded', function(){
    let hiddenField = document.createElement('input');
    hiddenField.type = 'hidden';
    hiddenField.name = 'exec_source';

    $('#exec').on('click', function() {
        hiddenField.value = editor.getValue();
        document.myform.appendChild(hiddenField);
        // console.log(editor.getValue());
        $.ajax({
            url: $(this).parent('form').attr('action'),
            type: 'post',
            data: $(this).parent('form').serialize()
        }).done(function(received_data) {
            // console.log(received_data);
            $("#result_text").html(received_data);
        }).fail(function() {
            console.log("失敗");
        });

        return false;
    });
});
