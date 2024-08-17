// static/src/js/custom_widget.js
"use strict";

odoo.define('your_module_name.custom_widget', function (require) {
    

    require('web.dom_ready')
    var core = require('web.core');
    var Widget = require('web.Widget');

    var CustomWidget = Widget.extend({
        start: function () {
            this._super();
            var ulElement = document.querySelector('.list-group.d-block.o_search_panel_field');
            if (ulElement) {
                var liElements = ulElement.getElementsByTagName('li');
                for (var i = 0; i < liElements.length; i++) {
                    var liElement = liElements[i];
                    var labelTitle = liElement.querySelector('.o_search_panel_label_title');
                    if (labelTitle && labelTitle.textContent.trim() === 'All') {
                        liElement.remove();
                        break;
                    }
                }
            }
        }
    });

    core.action_registry.add('your_module_name.custom_widget', CustomWidget);
});
