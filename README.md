<br/>
<p align="center">
  <h1 align="center">fontpocalypse</h1>

  <p align="center">
    A powerful tool for typography-based cyber security vulnerabilities. Generates custom fonts, CSS files, and HTML to visualize and explore security risks.
    <br/>
    <br/>
    <a href="https://jax.dev/fontpocalypse">View Demo</a>
    .
    <a href="https://github.com/anger/fontpocalypse/issues">Report Bug</a>
    .
    <a href="https://github.com/anger/fontpocalypse/issues">Request Feature</a>
  </p>
</p>



## Table Of Contents

- [Table Of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [Features](#features)
  - [Why Should You Care?](#why-should-you-care)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
  - [Creating A Pull Request](#creating-a-pull-request)
- [License](#license)

## About The Project

Fontpocalypse is a project aimed at raising awareness about the risks of copying and pasting arbitrary text found online without proper scrutiny. It demonstrates how attackers can leverage custom fonts to mask characters and deceive users.

### Features
- **Font Generation**: Generate custom fonts with hidden characters to simulate potential attacks.
- **CSS File Generation**: Create CSS files to apply the custom fonts to web pages.
- **HTML Span Generation**: Generate HTML spans using custom fonts to visually demonstrate character masking.

### Why Should You Care?
In the digital age, it's crucial to exercise caution when handling text from unknown sources. Cybercriminals can exploit typography-based vulnerabilities, utilizing custom fonts to mask characters and create malicious content. By raising awareness of these risks, fontpocalypse emphasizes the importance of verifying and validating text before using it, ultimately safeguarding against potential attacks.

## Getting Started


### Prerequisites

You must have [fontforge](https://fontforge.org/en-US/) installed to use fontpocalypse. That can be done [here](https://fontforge.org/en-US/downloads/), or if you use the apt package manager, with this command: `sudo apt-get install python3-fontforge`


### Installation

```bash
  git clone https://github.com/anger/fontpocalypse
  cd fontpocalypse
  fontforge -lang=py -script main.py 
```

## Usage

Once installed, you can run fontpocalypse with: ` fontforge -lang=py -script main.py `

You will be asked 4 questions. 

1. Enter the base font file (EX: comic-sans.ttf)                                 
2. Enter the CSS file name (EX: main.css)                                                                    
3. Enter the text to write (EX: hidden text)                                                                
4. Enter the text to see (EX: text hidden)
Both 3 & 4 must be the same amount of characters for it to work properly. 

## Contributing
### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/anger/fontpocalypse/blob/main/LICENSE.md) for more information.

![Contributors](https://img.shields.io/github/contributors/anger/fontpocalypse?color=dark-green) ![Issues](https://img.shields.io/github/issues/anger/fontpocalypse) ![License](https://img.shields.io/github/license/anger/fontpocalypse) 