import { Construct } from "constructs";
import { App, TerraformStack } from "cdktf";
import { } from '@cdktf/provider'

class MyStack extends TerraformStack {
  constructor(scope: Construct, name: string) {
    super(scope, name);

    // define resources here
  }
}

const app = new App();
new MyStack(app, "automation");
app.synth();
