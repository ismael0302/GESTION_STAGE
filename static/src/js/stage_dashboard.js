/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";

export class StageDashboard extends Component {
    setup() {
        // Tu peux ajouter des appels ORM ici
    }
}

StageDashboard.template = "gestion_stage.stage_dashboard";

registry.category("actions").add("stage_dashboard", StageDashboard);
