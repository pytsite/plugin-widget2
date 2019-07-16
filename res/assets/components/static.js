import PropTypes from 'prop-types';
import React from 'react';
import {Parser} from 'html-to-react';

export class Html extends React.Component {
    static propTypes = {
        html: PropTypes.string.isRequired,
    };

    render() {
        const p = new Parser();
        return p.parse(this.props.html);
    }
}
