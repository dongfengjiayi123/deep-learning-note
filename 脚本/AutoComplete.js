module.exports = async (params) => {
    const { quickAddApi } = params;

    // 定义自动补全的映射关系
    const autoCompleteMap = {
        "mbb": "\mathbb{B}",
        "dt": "due date",
        "td": "todo",
        "nt": "note template",
        "mb": "my bad",
        // 添加更多映射
    };

    // 获取当前光标位置的内容
    const editor = app.workspace.activeLeaf.view.editor;
    const cursor = editor.getCursor();
    const line = editor.getLine(cursor.line);
    const word = line.substring(0, cursor.ch).split(/\s+/).pop(); // 获取当前输入的词

    // 如果输入的词在映射中，则替换
    if (autoCompleteMap[word]) {
        const start = { line: cursor.line, ch: cursor.ch - word.length };
        const end = cursor;
        editor.replaceRange(autoCompleteMap[word], start, end);
    }
};