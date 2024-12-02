# Digital Trails Web

## Setup Local
To develop locally install Python and then run `pip install -r requirements.txt` in root.

This above command will install the `ark` SSG. For more information see https://www.dmulholl.com/docs/ark/main/.

## Build Local
To build the site locally run the `ark build` command in the project root.

After running `ark build` the folder `/out` will be generated. 

Navigate to the `/out` folder and run `ark serve` to see the site in a web browser.

You will need to run `ark build` again after every change to update the `ark serve` site.

## Adding New Pages
Add  `*.html` or `*.md` files to `src/`. These will be given headers and footers when Ark builds. 

## Modifying Site-Wide Content
To modify site wide content edit the `lib/templates/node.ibis` template (which wraps all `src` content).

## Adding Raw Assets 
The `res` folder is short for "resource" and contains raw assets to deploy in the root.

The `lib/v1/resources/assets` also contains assets that are required for the site layout.

## Adding Undeployed Content
The `undeployed` contains files that are useful to store with the website but don't need to deploy.

## Publishing Changes
All pushes to "main" will automatically trigger publication.

Publication can also be manually triggered in the GitHub Actions menu.
