
function getTextAreasString() {
    var textArray = []
    Array.from(document.getElementsByTagName("textarea")).forEach(
        textarea => textArray.push(textarea.textContent)
    )
    return textArray;
}
getTextAreasString()