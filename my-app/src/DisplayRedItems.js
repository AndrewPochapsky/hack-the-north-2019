import React, { Component } from 'react';

export class DisplayRedItems extends Component {

    render() {
        return (
			<div style={myStyle}>
                <h4>{this.props.subreddit.subred}</h4>
            </div>
		)
    }
}

const myStyle = {
    padding: '0.5vw 4vw',
    paddingBottom: '5vw',
    textAlign: 'center',
    fontFamily: 'white',
    fontSize: '25px',
    backgroundColor: 'black',
    color: 'white',
}

export default DisplayRedItems