import React, { Component } from 'react';

export class DisplayRedItems extends Component {

    render() {
        return (
            <div style={blackDiv}>
            <div style={textDiv}>
            <h1>{this.props.subreddit.id}</h1>
            </div>
			<div style={myStyle}>
                <h4>{this.props.subreddit.subred}</h4>
            </div>
            </div>
		)
    }
}

const myStyle = {
    padding: '.01vw 3vw',
    fontFamily: 'Quicksand',
    fontSize: '25px',
    backgroundColor: '#d9d9d9',
    color: 'black',
    borderRadius: '10px',
    width: '75%',
    float: 'right'
}

const blackDiv = {
    padding: '1vw 15vw',
    backgroundColor: 'black',
    color: 'white',
    height: '100px'
}

const textDiv = {
    width:'15%',
    float: 'left'
}



export default DisplayRedItems