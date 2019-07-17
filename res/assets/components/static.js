import PropTypes from 'prop-types';
import React from 'react';
import {Parser} from 'html-to-react';
import Widget from './widget';

export class Html extends Widget {
    static propTypes = Object.assign({}, Widget.propTypes, {
        html: PropTypes.string.isRequired,
    });

    render() {
        const p = new Parser();
        return p.parse(this.props.html);
    }
}
