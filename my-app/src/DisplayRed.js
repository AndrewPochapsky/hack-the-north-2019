import React, { Component } from 'react';
import DisplayRedItems from './DisplayRedItems';

export class DisplayRed extends Component {

    render() {
        return this.props.subreddits.map((subreddit) =>
            <DisplayRedItem key={subreddit.id} subreddit={subreddit}
            />);
    }
}

export default DisplayRed