"use strict";

/**
 * Color Palette Generator
 *
 * This application allows users to input a query or theme and receive a color palette
 * in response. Each color in the palette is presented as a block, and upon clicking
 * a color block, its hex code is copied to the clipboard. The user is provided with
 * visual feedback when a color is copied. There's also functionality to clear the
 * generated palette and input field, restoring the application to its initial state.
 *
 * Main functionalities:
 * - Fetching color palettes based on user input.
 * - Displaying the colors in a visually appealing manner.
 * - Allowing users to copy individual colors to the clipboard.
 * - Providing feedback upon copying a color.
 * - Resetting the application state with a clear button.
 */




/**
 * Main initialization and event bindings.
 */

// Reference to the form element
const form = document.querySelector("#form");

// Event listener for form submission
form.addEventListener("submit", function (e) {
  e.preventDefault();
  getColors();
});

/**
 * Fetches colors from the server based on the query.
 * Appends the received colors to the container.
 */
function getColors() {
  const query = form.elements.query.value;
  fetch("/palette", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams({
      query: query,
    }),
  })
  .then((response) => response.json())
  .then((data) => {
    const colors = data.colors;
    const container = document.querySelector(".container");
    createColorBlocks(colors, container);
  });
}

/**
 * Creates color blocks based on the provided colors and appends them to the container.
 * @param {Array} colors - Array of colors to be displayed.
 * @param {HTMLElement} container - Container where color blocks are to be appended.
 */
function createColorBlocks(colors, container) {
  container.innerHTML = "";
  for (const color of colors) {
    const div = document.createElement("div");
    div.classList.add("color");
    div.style.backgroundColor = color;
    div.style.width = `calc(100%/ ${colors.length})`;

    div.addEventListener("click", function () {
      navigator.clipboard.writeText(color);
      showCopiedFeedback(div);
    });

    const span = document.createElement("span");
    span.innerText = color;
    span.style.position = 'relative';
    div.appendChild(span);

    container.appendChild(div);
  }
}

/**
 * Displays a feedback message when a color is copied.
 * @param {HTMLElement} element - The clicked color div.
 */
function showCopiedFeedback(element) {
  const tooltip = document.createElement("div");
  tooltip.innerText = "Copied!";
  tooltip.style.position = "absolute";
  tooltip.style.bottom = "100%";
  tooltip.style.left = "50%";
  tooltip.style.transform = "translateX(-50%) translateY(-5px)";
  tooltip.style.padding = "5px 10px";
  tooltip.style.backgroundColor = "white";
  tooltip.style.color = "black";
  tooltip.style.borderRadius = "5px";
  tooltip.style.zIndex = "1";
  tooltip.style.fontSize = "0.9rem";

  const span = element.querySelector("span");
  span.appendChild(tooltip);

  setTimeout(() => {
    span.removeChild(tooltip);
  }, 1500);
}

/**
 * Main initialization for clearing the form and the color palette.
 */

// Reference to the clear button
const clearBtn = document.querySelector(".clear-btn");

// Event listener for the clear button
clearBtn.addEventListener("click", function() {
  form.elements.query.value = "";

  const container = document.querySelector(".container");
  container.innerHTML = `
    <div class="header-section">
    <h2>Color Palette Generator</h2>
      <p>Enter a few words to describe a palette you'd like to see. For example:</p>
      <p>"The Mona Lisa", "misty morning on the lake in spring", "Wes Anderson's 'The Life Aquatic'"</p>
      <p>You may submit the same prompt more than once to see various palettes, or clear the form to start a new prompt.</p>
      <p>If you see a color you love, click on it and it will be saved to your clipboard.</p>
      <h2>Tech Stack:</h2>
      <ul>
          <li><strong>Backend:</strong> Python &amp; Flask</li>
          <li><strong>AI:</strong> OpenAI GPT-3 API</li>
          <li><strong>Frontend:</strong> HTML (with DOM Manipulation) &amp; CSS</li>
          <li><strong>Deployment:</strong> Google App Engine</li>
      </ul>
    </div>
  `;
});


