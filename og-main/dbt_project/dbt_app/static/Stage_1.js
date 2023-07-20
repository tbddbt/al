function getColumnFormat_Stage_1() {
    var columns;
  
    columns = [
      {readOnly: true },
      {type: 'date', readOnly: true },
      {readOnly: true },
      {readOnly: true },
      {readOnly: true },
      {},
      {
        renderer: customDropdownRenderer,
        editor: "chosen",
        width: 150,
        chosenOptions: {
            multiple: true,
            data: ['1','2','3']
        }
      },{},{},{type: 'date',},{},{},{},{},{type: 'date',},{},{type: 'date',},{},{},{type: 'date',},
      {
        editor: 'select', 
        selectOptions: ['Accept','Reject'],
      },{},{type: 'checkbox'},
    ];
    return columns;
  }

function customDropdownRenderer(instance, td, row, col, prop, value, cellProperties) {
  var selectedId;
  var optionsList = cellProperties.chosenOptions.data;

  if(typeof optionsList === "undefined" || typeof optionsList.length === "undefined" || !optionsList.length) {
      Handsontable.cellTypes.text.renderer(instance, td, row, col, prop, value, cellProperties);
      return td;
  }

  var values = (value + "").split(",");
  value = [];
  for (var index = 0; index < optionsList.length; index++) {

      if (values.indexOf(optionsList[index].id + "") > -1) {
          selectedId = optionsList[index].id;
          value.push(optionsList[index].label);
      }
  }
  value = value.join(", ");

  Handsontable.cellTypes.text.renderer(instance, td, row, col, prop, value, cellProperties);
  return td;
}