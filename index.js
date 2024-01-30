import fs from 'fs';
import { PdfReader } from 'pdfreader';
import readline from 'readline';

const pdfFilePath = 'Sample.pdf';
function transformDataToKeyValuePairs(data) {
  const result = {};
  let currentKey = null;

  for (const item of data) {
    if (item.text.endsWith(":")) {
      currentKey = item.text.replace(/:$/, "").trim();
    } else if (currentKey !== null) {
      result[currentKey] = item.text.trim();
      currentKey = null;
    }
  }

  return result;
}

function displayRowWiseDetails(keyValuePairs) {
  console.log('Row-wise details:');

  // Add sample key-value pairs to the JSON object
  const allKeyValuePairs = {
    ...keyValuePairs,
    
  };

  // Display all key-value pairs
  Object.entries(allKeyValuePairs).forEach(([key, value]) => {
    console.log(`${key}: ${value || 'N/A'}`);
  });
}

function parsePdfAndRoundData(pdfFilePath) {
  return new Promise((resolve, reject) => {
    const pdfTextNew = [];
    if (!fs.existsSync(pdfFilePath)) {
      console.log('PDF file does not exist.');
      reject('PDF file does not exist.');
      return;
    }
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
    });

    new PdfReader().parseFileItems(pdfFilePath, (err, item) => {
      if (err) {
        console.log(err);
        reject(err);
      } else if (!item) {
        const keyValuePairs = transformDataToKeyValuePairs(pdfTextNew);

        fs.writeFileSync('output.json', JSON.stringify(keyValuePairs, null, 2));

        displayRowWiseDetails(keyValuePairs);

        rl.question('Enter the key to display its value: ', (userInput) => {
          const selectedValue = keyValuePairs[userInput];
          console.log(`${userInput}: ${selectedValue || 'Key not found'}`);
          rl.close();
        });

        resolve();
      } else if (item.text) {
        pdfTextNew.push({
          text: item.text,
          page: item.page,
        });
      }
    });
  });
}

parsePdfAndRoundData(pdfFilePath)
  .then(() => {
    // Do something if needed
  })
  .catch(error => {
    // Handle errors
  });
