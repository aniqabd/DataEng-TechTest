import React from "react";
import {
  SearchProvider,
  Results,
  SearchBox,
  Paging,
  Sorting,
  Facet,
} from "@elastic/react-search-ui";
import ElasticsearchAPIConnector from "@elastic/search-ui-elasticsearch-connector";
import "@elastic/react-search-ui-views/lib/styles/styles.css";

// Setup for the Elasticsearch API connector, specifying the server's API URL and the index to query
const connector = new ElasticsearchAPIConnector({
  host: "http://localhost:9200",
  index: "cv-transcriptions",
});

// Configuration for the search UI, including the connector and query specifics
// Generated Text is used as the primary query for the result
const configurationOptions = {
  apiConnector: connector,
  searchQuery: {
    search_fields: {
      generated_text: {},
    },
    result_fields: {
      generated_text: { raw: {} },
      duration: { raw: {} },
      age: { raw: {} },
      gender: { raw: {} },
      accent: { raw: {} },
    },
  },
  alwaysSearchOnInitialLoad: true,
};


// The main App component that renders the search UI
function App() {
  return (
    <div className="App">
      <SearchProvider config={configurationOptions}>
        <div className="search-header">
          <SearchBox />
        </div>
        <div className="search-results">
          <Results />
        </div>
        <div className="search-pagination">
          <Paging />
        </div>
        <div className="search-facets">
          <Facet field="generated_text" label="Generated Text" />
          <Facet field="duration" label="Duration" />
          <Facet field="age" label="Age" />
          <Facet field="gender" label="Gender" />
          <Facet field="accent" label="Accent" />
        </div>
      </SearchProvider>
    </div>
  );
}

export default App;
