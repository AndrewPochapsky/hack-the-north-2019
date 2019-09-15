import React, { Component } from 'react';
import Header from './components/Header';
import Description from './components/Description';
import Description2 from './components/Description2';
import DisplayRed from './DisplayRed';
import AddPost from './AddPost';
class App extends Component {

    state = {
        isSubmit: true,
            subreddits: [
                {
                    id: 1,
                    subred:"red1",
                    link:"http://www.fuck"
                },
                {
                    id: 2,
                    subred: "red2",
                    link: "http://www.fuck"
                },
                {
                    id: 3,
                    subred: "red3",
                    link: "http://www.fuck"

                },
                {
                    id: 4,
                    subred: "red4",
                    link: "http://www.fuck"
                },
                {
                    id: 5,
                    subred: "red5",
                    link: "http://www.fuck"
                }
            ]
    }

    render() {
        if ( this.state.isSubmit === false) {
            return (
                <div className="App">
                    <Header />
                    <Description />
                    <AddPost />
                </div>
            );
        } else {
            return (
                <div className="App">
                    <Header />
                    <Description2 />
                    <DisplayRed subreddits={this.state.subreddits}/>
                </div>
            );

        }
    }
}

export default App;
