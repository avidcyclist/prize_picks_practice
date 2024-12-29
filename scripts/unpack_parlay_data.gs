function unpackJsonData() {
  // Get the active spreadsheet and the source sheet
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sourceSheet = ss.getSheetByName("mock_user_picks.csv"); // Replace with your source sheet name
  var targetSheet = ss.getSheetByName("unpacked_parlays"); // Replace with your target sheet name or create a new one

  // Get the data from the source sheet
  var data = sourceSheet.getRange("I2:I10001").getValues(); // Assuming your JSON data is in column I starting from row 2

  // Clear the target sheet
  targetSheet.clear();

  // Set headers in the target sheet
  var headers = ["Pick_ID", "User_ID", "Player_ID", "Stat_Type", "User_Pick", "Projection", "Actual_Stat", "Result", "Single_Odds"];
  targetSheet.getRange(1, 1, 1, headers.length).setValues([headers]);

  // Loop through the data and unpack the JSON
  var unpackedData = [];
  for (var i = 0; i < data.length; i++) {
    if (data[i][0]) {
      try {
        Logger.log("Processing row " + (i + 2) + ": " + data[i][0]);
        var jsonDataArray = JSON.parse(data[i][0].replace(/'/g, '"')); // Replace single quotes with double quotes for valid JSON
        for (var j = 0; j < jsonDataArray.length; j++) {
          var jsonData = jsonDataArray[j];
          var row = [
            jsonData.Pick_ID,
            jsonData.User_ID,
            jsonData.Player_ID,
            jsonData.Stat_Type,
            jsonData.User_Pick,
            jsonData.Projection,
            jsonData.Actual_Stat,
            jsonData.Result,
            jsonData.Single_Odds
          ];
          unpackedData.push(row);
        }
      } catch (e) {
        Logger.log("Error parsing JSON at row " + (i + 2) + ": " + e.message);
      }
    }
  }

  // Write the unpacked data to the target sheet
  if (unpackedData.length > 0) {
    targetSheet.getRange(2, 1, unpackedData.length, headers.length).setValues(unpackedData);
  } else {
    Logger.log("No data to write to the target sheet.");
  }
}