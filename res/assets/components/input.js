import PropTypes from 'prop-types';
import React from 'react';

export class Input extends React.Component {
    static propTypes = {
        autoComplete: PropTypes.string,
        autoFocus: PropTypes.bool,
        className: PropTypes.string,
        enabled: PropTypes.bool,
        required: PropTypes.bool,
        readOnly: PropTypes.bool,
        type: PropTypes.string,
    };

    static defaultProps = {
        type: 'hidden',
    };

    render() {
        return <input {...this.props}/>;
    }
}

export class Hidden extends React.Component {
    render() {
        return <Input type={'hidden'} {...this.props}/>;
    }
}

export class Text extends React.Component {
    render() {
        return <Input type={'text'} {...this.props}/>;
    }
}
