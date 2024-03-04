## Prestudy

- Roles of Back-End, Front-End, Full-Stack engineers
- Internet technologies
    - HTTP
- HTML5 and CSS
- Bootstrap, UI frameworks
- React


## Time
4w 4-8 h = 16-32 h (18 h on the certificate page)
<3h video + 4+ h reading = 7h material
7 graded + Labs

## 1 WEEK web basics
### How the Web Works
- Intro
    - Intro to Program
    - Intro to course
        - roles
        - HTML, CSS, Js
        - Bootstrap, UI, React
        - Biography page
        - Website/Webapp, Webserver, Browser
    - Roles
        - Front-End - appearance and visual functionality. (core HTML, CSS, JS)
            - JS - have libraries
        - Back-End - non-visual functionality.
            - Databases
            - Back-end language
            - Network
            - APIs
        - Full-Stack
    - Capstone Project at the end of the program (Dynamic restaurant webapp)
- Internet
    - Interconnected networks
        - Switches
    - Server - Client
        - Data Centers or Many in the internet
        - Webserver
            - Security
            - Web ...
            - Data storage
            - ...
        - Request to server - Response from the server
- Web pages and Web sites
    - Web page - a document with different types of content
    - Web site - collection of web pages linked with each other with the same address
        - HTML - structure
        - CSS - decorations
        - JS - interaction
    - Page rendering by web browser 
- Web browser - software that helps to surf througout the Internet
    - Protocol://domainname/filepath - url bar
    - HTTP Response - Request Cycle
    - Rendering page
- Web hosting - place where you can put your website
    - Shared Hosting - shares resources with outher websites
    - VPS - Virtual Private Server - dedicated resources but several on the same hardware
    - Dedicated - dedicated hardware
    - Cloud - combination of VPS and physical servers - cloud environment. Fault tolerance
- Additional
    - [What is a Web Server? (NGINX)](https://www.nginx.com/resources/glossary/web-server/)
    - [What is a Web Browser? (Mozilla)](https://www.mozilla.org/en-US/firefox/browsers/what-is-a-browser/)
    - [Who invented the Internet? And why? (Kurzgesagt)](https://youtu.be/21eFwbb48sE)
    - [What is Cloud Computing? (Amazon)](https://youtu.be/mxT233EdY5c)
    - [Browser Engines (Wikipedia)](https://en.wikipedia.org/wiki/Browser_engine)

### Core Internet Technologies
- IP protocol
    - IPv4 and IPv6 address
    - IP packet
        - Header
            - Destination and Source addresses
        - Data
    - Other protocols
        - Problems when delivering IP packets
            - Out of order
            - Damaged
            - Lost
        - TCP - solve all problems - When data should be correct (websites)
        - UDP - do not solve - When we can sacrifice some packets (live streaming)
- HTTP - HyperText Transfer Protocol - Request-Response protocol
    - Transfer web pages, files and images and other resourses
    - Request structure
        - Method
            - GET
            - POST
            - PUT
            - DELETE
            - PATCH
        - Path
        - Version
        - Headers
    - Response structure
        - Same but with
            - Status code. Status Message
                - 100-199 - Informational
                    - 100 - Continue
                    - 101 - Switching protocols
                - 200-299 - Successful
                    - 200 - OK
                    - 201 - Created
                    - 202 - Accepted
                    - 204 - No content
                - 300-399 - Redirection
                    - 301 - Moved Permanently
                    - 302 - Moved Temporary (Found)
                - 400-499 - Client Side Error
                    - 400 - Bad Request
                    - 401 - Not Authorized
                    - 403 - Forbidden
                    - 404 - Page Not Found
                    - 405 - Method Not Allowed
                - 500-599 - Server Side Error
                    - 500 - internal server error
                    - 502 - Bad Gateway
                    - 503 - Service Unavailable
    - HTTPS - secure because of encryption
        - SSL certificate
    - More detail of HTTP
        - Request
            - Request line - Method Path Version
            - Headers
                - Host - host of the server
                - User-Agent - informs about client application (OS + browser info)
                - Accept - type of content that client will accept
                - Accept-Language
                - Content-type - content in the request body
            - Request Body
        - Response
            - Status Line - HTTP/Version Status_Code Status_message
            - Headers
                - Date
                - Server - server software information
                - Content-Length
                - Content-Type
            - Response Body
- **HTML/CSS/JS intro**
    - Clock app
        - HTML for displaying numbers
        - CSS to style fonts, background, position
        - JS to dynamically change the value on the clock
    - Video playing app
        - HTML to register video and button
        - CSS to style it: position, colors
        - JS - register listener on button that check if it pressed and than check 
            the state of the video(playing or stopped)
- Other Internet Protocols
    - HTTP works on top of TCP
    - DHCP - Dynamic Host Configuration Protocol. DHCP server used to give network clients IP addresses
    - DNS - Domain Name System. DNS servers used to convert domain name to IP address
    - IMAP - Internet Message Access Protocol. Used by email client (some app on the device) to download emails from email server.
    - SMTP - Simple Mail Transfer Protocol. Used by email client to submit emails.
    - POP - Post Office Protocol. Same as IMAP but deletes emails on the server after downloading. Automation of email (easir)
    - FTP - File Transfer Protocol. FTP client and FTP server used to transmit files from server to client.
    - SSH - Secure . SSH protocol used to securely connect to server.
    - SFTP - Secure FTP or SSH FTP. FTP by default is not secure.
- Webpage Website Web application differences
    - Webpage - HTML, CSS, JS documents < Website
    - Web app and Website are the same but have differences
        - Web app is more interactive - f.e. personalized information, location check, update content
            - different for different users
        - Web site is more informative - f.e. information about some company
- Developer tools
    - Changing code in the browser
- Framework and Libraries
    - Library
        - re-usable
        - specific purpose
        - You call the library code
        - Easier to change to another
    - Framework
        - contains a set of libraries
        - Structure for developing application
        - Calls your code
        - Hard to change to another
        - Compatibility with other libraries
- APIs and Services
    - API - gateway - the bridge between computers (middleware) App Programming Interface
    - Browser API
    - RESTful API - representational state transfer - Communication between server and client
        - common methods: GET, POST, PUT, DELETE
        - common answers: web page, json (some information)
    - Sensor API - internet of things
- IDE - toolbox for developers (Integrated Development Environment)
    - Keywords Highlighting
    - Errors Highlingting
    - Autocomplete and IntelliSense
    - Refactoring
    - Downloading IDE and how to use Labs

### 1w Summary
- Webpages
    - Website and Webpage
    - HTML CSS Javascript
- Webserver
    - Data centers
    - Web server hardware and software
    - HTTP
    - Request-Response cycle
- Web browser
    - Request-Response cycle
    - Page rendering
    - Browser server interaction
    - Developer tools
- Website Webapp
- Frontend, Backend
- Libraries and Frameworks
- API
- IDE
- IP and data transfer

- Additional Resources
    - [HTTP Overview (Mozilla)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
    - [Introduction to Networking by Dr.Charles R Severance](https://www.amazon.com/Introduction-Networking-How-Internet-Works/dp/1511654945/)
    - [Chrome Developer Tools Overview (Google)](https://developer.chrome.com/docs/devtools/overview/)
    - [Firefox Developer Tools User Docs  (Mozilla)](https://firefox-source-docs.mozilla.org/devtools-user/index.html)
    - [Getting Started with Visual Studio Code  (Microsoft)](https://code.visualstudio.com/docs)


## 2 WEEK HTML/CSS basics
### Getting Started with HTML
- HTML - HyperText(links) Markup(tags) Language
    - open-close tags (p, h)
    - self-closing tags (br, img)
- Base structure
```html
<!DOCTYPE html>
<html>  <!-- root -->
    <head>
        <!-- meta data, title, links to other files -->
    </head>
    <body>
        <!-- page content -->
    </body>
</html>
```
- Tags
    - html, head, body
    - title
    - p, h1-h6, img, br
    - strong(importance), bold(attention)
    - em(emphasis), i - italic(off set text (f.e. titles))
    - span
    - ul, ol
        - li
    - div - division of content
    - \<!-- comments -->
    - a
        - *href*
    - img
        - *src*
        - *width, height*
        - *alt*
    - table
        - tr
            - th, td
    - style - tag for css
    - form - making http requests
        - *action, method (POST, GET)*
        - label
            - *for* name
        - input
            - *type* (text, password, submit, checkbox, radio, number, email, file)
            - *name*
            - *value* for checkboxes and radio buttons
        - select
            - option
                - *value*
        - textarea
            - *rows*
- **DOM** - Document Object Model - representation of html document in js
    - Tree of html tags
    - Used by JavaScript to manipulate html elements
        - f.e. change value on the stopwatch
        - Create animation, popups for messages and so on
- **LAB: Creating HTML Document**
- WAI - Web Accessibility Initiative
    - Creating environment for people with disabilities to be able to understand content
        - Speech Recognition
        - Screen reader
        - Subtitles
    - Propper usage of HTML
    - ARIA specification
- Test
- Additional Resources
    - [HTML Elements Reference (Mozilla)](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)
    - [The Form Element (Mozilla)](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)
    - [What is the Document Object Model? (W3C)](https://www.w3.org/TR/WD-DOM/introduction.html)
    - [ARIA in HTML (W3C via Github)](https://w3c.github.io/html-aria/)
    - [ARIA Authoring Practices  (W3C)](https://www.w3.org/TR/wai-aria-practices-1.2/)

### CSS basics
- Preview extension
- CSS - style of the web page (how it is shown)
    - link tag to link file to html
        - *rel, href*
    - CSS rule
        - Selector
            - Precedence
                - tag -> class -> id
            - Examples
                - element, .class, #id(unique through page)
                - element + class or id (p.someclass)
                - descedant (div p i), child(div > h1)
                - pseudo-classes
                    - hover
        - Declaration Block
            - Properties and Values
                - **text and color**
                    - color: *rgb(), rgba(), hsl() *- hue saturation lightness, *hex*.
                    - font-family
                    - font-size
                    - text-transform
                        - *uppercase, lowercase, capitalize, none*
                    - text-decoration: *line color style thickness*
                        - text-decoration-line, text-decoration-color ...
                        - line: *underline, overline, line-through, none*
                        - style: *solid, dotted, double, dashed, wavy*
                - **box-model tags**
                    - width, height, max/min-width/height
                    - padding or padding-left/right/top/bottom
                    - border: *width style color* or
                        - border-width: *thin/medium/thick*
                        - border-style: *dotted, solid, dashed, double*
                        - border-color
                    - border-left/right/top/bottom
                    - border-radius: px
                    - margin or margin-left/right/top/bottom
                - **Document Flow**
                    - display: *inline/block* (to element)
                    - Element Alignment
                        - center
                            - define width and make left&right margins auto so it fills parent
                            - if it's not a block element => **display: block;**
                        - left, right
                            - float: *left/right*
                            - position
                    - Text Alignment
                        - text-align: *center/left/right/justify*
- Box Model - content of page located in boxes
    - content, padding, border, margin box sizes
    - padding and border make element bigger
    - margin - space between elements
- Document Flow
    - Block vs Inline
        - Block Tags occupy all width of the parent: div, p, form, h1-h6 
        - Inline Tags occupy width of content: a, img, input, em, i, b, strong, span, label
- Test
- **LAB: Styling a page**
- Additional Resources
    - [CSS Reference (Mozilla)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference)
    - [HTML and CSS: Design and build websites by Jon Duckett](https://www.amazon.com/HTML-CSS-Design-Build-Websites/dp/1118008189/)
    - [CSS Definitive Guide  by Eric Meyer](https://www.amazon.com/CSS-Definitive-Guide-Visual-Presentation/dp/1449393195/)

### Creating a web page
- **Creating and styling a web page**
- Module Quiz: Introduction to html and CSS

### Summary
- HTML
    - Basic documents, html tags
    - Links, forms, tables
- Accessibility
- DOM
    - JS manipulation (updating, setting events, animations)
- CSS
    - CSS rules
    - CSS box-model
- **BIOGRAPHICAL PAGE**


## 3 WEEK UI Frameworks/React
### UI Frameworks and Libraries => Bootstrap
- Dependencies (libraries and frameworks)
    - Example of linking <u>***bootstrap***</u> library
    - Dependency Tree
        - Package Manager - helps to manage packages (dependencies) so you can easily install packages without dependency issues
            - Node Package Manager (NPM)
    - Adding dependencies to html file can be forever
        - Bundling tool (Bundle up) - creating one file for all dependencies
            - Webpack, Gulp
- Responsive Design - different screens
    - Pixels and modern phones with logical pixels
    - 3 main practices
        - Flexible Grids - columns, margins, gutters
            - No pixel orientated
            - Percentages
        - Fluid Images
            - max-width: 100% => not increased when stretched and fit into smaller block
        - Media queries - conditional css rules
            - Aspect ratio
            - Orientation
            - Display size
    - Responsive Grid - breakpoint
        - Fixed Grid
        - Fluid Grid
        - Hybrid grid
```css
@media only screen and (max-width: 700px) {
    body {
    }
}
```
- Bootstrap - Front-end framework
    - components
    - premade sets of rules for *responsive grid*
    - Getting started classes
        - container (Grid system)
            - row
            - col
        - img-fluid
        - table
    - class infix - breakpoints for grid system css rules
        - extra small
        - small sm
        - medium md
        - large lg
        - extra large xl
        - extra extra large xxl
    - modifiers
        - primary, secondary, success, danger, light, dark, info, warning
        - alerts
    - Grid
        - container, row, col - main parts of grid system
        - 12 columns
        - col-num - number of column for an html element
        - col-lg-num col-num - two classes work differently for different sizes
- **LAB: Working with bootstrap grid**
    - Lab self review
- Bootstrap Components - ready blocks of code
    - new dish fried calamari added to little lemon site
    - badge bg-primary
    - card
        - card-img-top
        - card-body (text content)
        - card-title
        - card-text
    - alert alert-info + role alert
- **LAB: Working with bootstrap components**
- [Bootstrap documentation](https://getbootstrap.com/docs)
    - Layout
    - Content
    - Forms
        - Form styling
        - Switches
        - input groups
        - floating labels
    - Components
- Other CSS Frameworks and libraries
    - Foundation
    - Pure.css
    - Tailwind CSS
    - UIKit
    - MVP css
- Additional Resources
    - [Bootstrap Official Website](https://getbootstrap.com/)
    - [Bootstrap 5 Foundations by Daniel Foreman](https://www.amazon.com/Bootstrap-Foundations-Mr-Daniel-Foreman/dp/B0948GRS8W/)
    - [Responsive Web Design with HTML5 and CSS  by Ben Frain  ](https://www.amazon.com/Responsive-Web-Design-HTML5-CSS/dp/1839211563/)
    - [Bootstrap Themes](https://themes.getbootstrap.com/)


### Introduction to React
- Static and Dynamic content
    - Application server -> Web server -> client
    - Application server
        - Communicate with DB
        - Check permissions
    - Caching for helping application server to manage more requests
- SPA - single page application
    - One html page that updates content
        - rewrites current page
    - 2 approaches
        - Bundling - all resources
        - Lazy loading - dynamically as required
    - Web server sends not full page but f.e. json
        - Templates or Pages
    - Views
- React - JS **library**
    - SPA and mobile applications
    - Navigation and requests
    - Easy to write code and test it
    - Components - a small piece of UI - you can build them by yourself
        - Isolated developing and testing + re-use
        - Libraries with pre-made components
- **MVC - model-view-controller**
    - React isn't an MVC framework
    - Doesn't use templates => components
    - render method - view representation => [reconcilitation](https://jsfiddle.net/uf3sr8L7/)
    - [JSX extension](https://legacy.reactjs.org/docs/jsx-in-depth.html)
- How React works?
    - Browser constructs DOM when receiving web page and browser rebuild it every change
    - REACT constructs a virtual DOM that keeps up to date
        - When some node need to be updated it change virtual DOM and compares it with prev version => reconcilitation
        - Than it changes the Browser DOM without rebuilding entire DOM tree
    - The virtual DOM
        - React checks if virtual DOM similar to browser DOM
        - if not similar => reconcilitation
            1. Virtual DOM updated
            2. The virtual DOM compared to its previous version to find out what element was changed
            3. The browser DOM is updated
            4. The web page updates to match the browser DOM
        - So the browser DOM changes when needed
        - But event can change a lot of elements => React Fiber Architecture
            - React spread update "over time"
                - changes only visible elements
                - optimization when and where to make DOM updates
            - Meta react developer tools.
    - Component Hierarchy and reusability
        - same as DOM
- React and complimentary libraries
    - lodash - for working with arrays, numbers, strings etc (utility lib)
    - Luxon - DateTime library
    - Redux - helps to manage a website state
    - Axios - HTTP request response handler
    - Jest - Testing library

### Summary
- Dependencies, Package Managers, Bundlers
- Responsive Web Design
- UI Frameworks and Libraries
    - Boost
        - grid, components
        - Boost CSS library
        - Infixes and modifiers
- React
    - Static and Dynamic content
    - web server, application server
    - Purpose of React
    - Components
    - Component Hierarchy
- Additional Resources
    - [React Official Website](https://reactjs.org/)
    - [Choosing between Traditional Web Apps and Single Page Apps (Microsoft)](https://docs.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/choose-between-traditional-web-and-single-page-apps)
    - [React Source Code (Github)](https://github.com/facebook/react)
    - [Introduction to React.js](https://youtu.be/XxVg_s8xAms)


## 4 WEEK - Recap
### Recap
- Introduction
    - HTML, CSS, JS basics and purpose
    - Client, Server, Browser
    - HTTP requests and responces, IP, TCP protocols
    - Front-End Back-End and Full-Stack engineers
    - IDE
- HTML, CSS
    - tags, DOM
    - Selectors, Properties and values
    - Web Accessibility
- UI libraries
    - Dependencies, Packer Managers, Bundlers
    - Boost - CSS library
        - Boost Grid, Infixes, Modifiers 
    - Responsive Design
    - React - JS library
        - Virtual DOM
        - Components and its hierarchy

### Ungraded LAB
- 2 column page
    - left - photo
    - right - Favourite music artists, films and meta profile
- There is an opened solution on the coursera


## Questions
- Complete all labs by yourself (create challenges to practice technologies)
- Bootstrap Themes?