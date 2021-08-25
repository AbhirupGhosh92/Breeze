const plugin = BaklavaJS.createBaklava(document.getElementById("editor"));
const editor = plugin.editor;

const myNode = new BaklavaJS.Core.NodeBuilder("My Node")
    .addInputInterface("My Interface")
    .build();
editor.registerNodeType("My Node", myNode);


