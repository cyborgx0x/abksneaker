// App.jsx
import React from "react";
import Hello from "./Hello";

var $ = require('jquery');

export default class App extends React.Component {
  render() {
    return (
      <div>
        <div className='header-content'>
          <Hello name="Rimini" />
        </div>
       </div>
    );
  }

}
