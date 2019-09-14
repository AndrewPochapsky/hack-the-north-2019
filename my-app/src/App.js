import React, { Component } from 'react';
import Header from './components/Header';
import Description from './components/Description';
import AddPost from './AddPost';
class App extends Component {
    render() {
        //console.log(this.state.todos)
        return (
            <div className="App">
                <Header />
                <Description />
                <AddPost />
            </div>
        );
    }
}

export default App;
