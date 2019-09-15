import React, { Component } from 'react';
import Header from './components/Header';
import Description from './components/Description';
import Description2 from './components/Description2';
import DisplayRed from './DisplayRed';
import AddPost from './AddPost';
import axios from 'axios';

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
                    title: '',
                    description: '',
                    isSubmit: false,
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
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(e) {

        "setting is submit to true";
        e.preventDefault();
        this.setState({isSubmit:true});

        const title = e.target.elements.title.value;
        const description = e.target.elements.description.value;
        console.log(title, description);
        axios.post('http://localhost:8000/api/createInput/', {
            title: title,
            description: description
        });

        //this.setState({this.props.isSubmit:true});
        // .then(res => console.log(res))
        // .catch(err => console.err(error));
    }


    render() {
        console.log("this.state.isSubmit", this.state.isSubmit);
        if ( this.state.isSubmit === false) {
            return (
                <div className="App">
                    <Header />
                    <Description />
                    <AddPost handleSubmit={this.handleSubmit} />
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
