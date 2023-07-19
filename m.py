# Update the "material.js" file:
# Modify the source property of the third column configuration to fetch the material types dynamically from the "material" sheet.
# Here's an example of how you can update the "material.js" file:

# javascript
# Copy code
# function getColumnFormat_Materials() {
#     var columns;

#     columns = [
#         { readOnly: true },
#         {},
#         {
#             editor: 'select',
#             source: function(query, process) {
#                 // Fetch the material types from the "material" sheet dynamically
#                 // You need to implement the logic to fetch the material types from the "material" sheet
#                 // and pass them to the process function
#                 var materialTypes = []; // Array to store material types
#                 $.ajax({
#                     url: '/path/to/material/sheet', // Replace with the URL to fetch the material sheet data
#                     method: 'GET',
#                     success: function(response) {
#                         // Extract material types from the response and populate the materialTypes array
#                         materialTypes = response.materialTypes;
#                         process(materialTypes);
#                     },
#                     error: function() {
#                         console.log('Error fetching material types');
#                     }
#                 });
#             }
#         },
#         { type: 'numeric', numericFormat: { pattern: '0' }, validator: positiveIntegerValidator },
#         {},
#         { type: 'date' },
#         {},
#         { type: 'date' },
#         { type: 'numeric', numericFormat: { pattern: '0' }, validator: positiveIntegerValidator },
#         {},
#         { type: 'date' },
#         { type: 'numeric', numericFormat: { pattern: '0' }, validator: positiveIntegerValidator },
#         {},
#         { type: 'checkbox' }
#     ];

#     return columns;
# }

# /====================

# In this updated code:

# The source property of the third column configuration uses an AJAX request to fetch the material types from the "material" sheet dynamically. Update the URL /path/to/material/sheet with the actual URL to fetch the material sheet data.
# Upon successful retrieval of the material types, the process function is called to pass the material types as options for the dropdown.
# Update the "stage1.js" file:
# Update the selectOptions property of the second column configuration to use the material types fetched from the "material" sheet.
# Here's an example of how you can update the "stage1.js" file:

# javascript
# Copy code

function getColumnFormat_Stage_1() {
    var columns;

    columns = [
        { readOnly: true },
        { type: 'date', readOnly: true },
        { readOnly: true },
        { readOnly: true },
        { readOnly: true },
        {},
        {
            editor: 'select',
            selectOptions: function() {
                // Fetch the material types from the "material" sheet dynamically
                // You need to implement the logic to fetch the material types from the "material" sheet
                // and return them as options for the dropdown
                var materialTypes = []; // Array to store material types
                $.ajax({
                    url: '/path/to/material/sheet', // Replace with the URL to fetch the material sheet data
                    method: 'GET',
                    async: false, // Ensure the options are available synchronously
                    success: function(response) {
                        // Extract material types from the response and populate the materialTypes array
                        materialTypes = response.materialTypes;
                    },
                    error: function() {
                        console.log('Error fetching material types');
                    }
                });
                return materialTypes;
            }
        },
        {},
        // ... rest of the column configurations
    ];

    return columns;
}
# In this updated code:

# The selectOptions property of the second column configuration is modified to use an anonymous function that fetches the material types from the "material" sheet dynamically.
# Similar to the "material.js" file, update the URL /path/to/material/sheet with the actual URL to fetch the material sheet data.
# The AJAX request is set to be synchronous (async: false) to ensure that the material types are available before returning the options for the dropdown.
# Please note that you need to implement the server-side logic to handle the AJAX requests and provide the material types in the response. Adjust the code according to your project's structure and requirements.