var frenchLaws = require("../dataset/code-construction-habitation-all")
var articlesWithParent = []
var articleRow = {}
var parentID = ["", "", "", "", "", "", "", "", "", "", "", ""] // get max depth to create the array -> 9
getDepth = function (obj, depth) {
  if (obj.children) {
    obj.children.forEach(function (d) {
      depth += 1
      if (d.type === "article") {
        // Uniquement article here
        // if(getParentId.length == 0)
        articleRow = { "articleText": d.data.texte, "articleTextHTML": d.data.texteHtml, "articleId": d.data.id, "listParentId": parentID.slice(1, depth)}
        articlesWithParent.push(articleRow)
        articleRow = {}
      }
      else {
        // Get only parent ID
        // parentID[depth] = d.data.id
        // Get parent ID and Title
        parentID[depth] = { "parentId": d.data.id, "parentTitle": d.data.title }
        getDepth(d, depth)
      }
      depth -= 1
    })
  }
  // Get id des parents here
}

getDepth(frenchLaws.json, 0)
const fs = require('fs')
// fs.writeFile(
//   "../dataset/generated-for-es-with-parentid-array.json",
//   JSON.stringify(articlesWithParent),
//   err => {
//     // In case of a error throw err.
//     if (err) throw err;
//   }
// );
fs.writeFile(
  "../dataset/generated-for-es-with-parent-as-object.json",
JSON.stringify(articlesWithParent),
  err => {
    if (err) throw err;
  }
)