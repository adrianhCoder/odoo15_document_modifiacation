odoo.define('my_module.kanban_renderer_alert', function (require) {
    "use strict";

    var KanbanRenderer = require('web.KanbanRenderer');

    KanbanRenderer.include({
        /**
         * Override the _renderView method to show an alert when rendering the Kanban view.
         * @override
         */
        _renderView: function () {
            // Show an alert when the Kanban view is being rendered
          //  alert('Kanban view is being rendered!');

            // Call the original _renderView method
            return this._super.apply(this, arguments);
        }
    });
});
