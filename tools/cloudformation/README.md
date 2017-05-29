 # That App Idea - Cloudformation Tools
 
## Initializing a stack
 
 Run a command line like this to create a new environment. This initialization 
 step will create the different dns records and keys required to manage the
 resources of the environment.
 
     ./initialize-stack -r eu-west-1 \
     --external-domain-name thisapp-lab.itcant.be \
     --internal-domain-name thisapp-lab --profile wakaru --project thisapp \
     --environment lab 

## Creating stacks inside the VPC

Once the stack is initialized, we can create the resources inside it.

