import PropTypes from 'prop-types';
import React from "react";
import ReactDOM from "react-dom";
import $ from "jquery";
import {Hidden} from "./components/input";

const widgets = {};

class ReactWidget extends React.Component {
    static propTypes = {
        wComponent: PropTypes.func.isRequired,
        wProps: PropTypes.object,
        wChildren: PropTypes.arrayOf(PropTypes.object),
    };

    render() {
        const children = [];
        this.props.wChildren.forEach(childInfo => {
            children.push(createWidget(childInfo['cid'], childInfo['props'], childInfo['children']));
        });

        return <React.Fragment>
            {React.createElement(this.props.wComponent, this.props.wProps, ...children)}
        </React.Fragment>;
    }
}

export function registerWidgetComponent(cid, widgetComponent) {
    widgets[cid] = widgetComponent;
    initComponents(cid);
}

export function createWidget(cid, props, childrenInfo) {
    if (!widgets.hasOwnProperty(cid))
        throw `Component for widget '${cid}' is not registered`;

    return <ReactWidget wComponent={widgets[cid]} wProps={props} wChildren={childrenInfo}/>;
}

/**
 * Hydrate an HTML element with component
 *
 * @param element
 */
export function hydrateElement(element) {
    const em = $(element);
    const cid = em.data('cid');
    const props = em.data('props');
    const children = em.data('children');

    if (em.hasClass('initialized'))
        return;

    ReactDOM.render(createWidget(cid, props, children), element);
    em.addClass('initialized');
}

function initComponents(cid) {
    // Init all widgets found on the page
    $(`.pytsite-widget2[data-cid="${cid}"]`).not('.initialized').each(function () {
        hydrateElement(this);
    });
}

// Register widgets provided by this plugin
registerWidgetComponent('plugins.widget2.input.hidden', Hidden);
