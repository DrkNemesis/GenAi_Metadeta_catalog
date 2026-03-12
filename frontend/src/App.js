import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {

  const [metadata, setMetadata] = useState([]);
  const [description, setDescription] = useState("");

  const loadMetadata = async () => {
    const res = await axios.get("http://127.0.0.1:8000/metadata");
    setMetadata(res.data);
  };

  const generateDescription = async (table, column, datatype) => {

    const res = await axios.post(
      "http://127.0.0.1:8000/generate-description",
      {
        table: table,
        column: column,
        datatype: datatype
      }
    );

    setDescription(res.data.description);
  };

  return (
    <div style={{padding:"40px"}}>

      <h1>AI Powered Data Catalog</h1>

      <button onClick={loadMetadata}>
        Load Metadata
      </button>

      <table border="1" style={{marginTop:"20px"}}>
        <thead>
          <tr>
            <th>Table</th>
            <th>Column</th>
            <th>Datatype</th>
            <th>AI Description</th>
          </tr>
        </thead>

        <tbody>
          {metadata.map((row,index) => (
            <tr key={index}>
              <td>{row.table_name}</td>
              <td>{row.column_name}</td>
              <td>{row.data_type}</td>

              <td>
                <button
                  onClick={() =>
                    generateDescription(
                      row.table_name,
                      row.column_name,
                      row.data_type
                    )
                  }
                >
                  Generate AI
                </button>
              </td>

            </tr>
          ))}
        </tbody>
      </table>

      <br/>

      <h3>AI Description</h3>
      <p>{description}</p>

    </div>
  );
}

export default App;