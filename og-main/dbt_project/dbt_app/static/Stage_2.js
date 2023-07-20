function getColumnFormat_Stage_2() {         
    var columns;
    
        columns = [
        {readOnly: true },{type: 'date',readOnly: true },{readOnly: true },{readOnly: true },{readOnly: true },{readOnly: true },
        { 
            editor: 'select', 
            selectOptions: ['Option 1', 'Option 2', 'Option 3'],
        },
        {type: 'date',},{},{},{},{},{type: 'date',},{},{},{type: 'checkbox'},
        ];
        return columns;
     } 