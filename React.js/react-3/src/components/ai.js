import { InferenceClient } from "@huggingface/inference";

// ✅ Your Hugging Face access token (safe for dev / local projects)
const HF_TOKEN = "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";

// Create the Hugging Face inference client
const client = new InferenceClient(HF_TOKEN);

/**
 * Generate a recipe based on ingredients
 * @param {string[]} ingredientsArr - list of ingredients
 * @param {string} model - optional, defaults to a good instruction model
 */
export async function getRecipeFromModel(
  ingredientsArr,
model = "google/gemma-2b-it"
) {
  const SYSTEM_PROMPT = `
You are a helpful AI chef.
The user will give you a list of ingredients.
Suggest one delicious recipe using some or all of them.
You can add a few extra ingredients if necessary, but keep it realistic.
Return the recipe in Markdown format (with a title, ingredients, and steps).
  `;

  const ingredientsString = ingredientsArr.join(", ");

  try {
    const response = await client.textGeneration({
      model,
      inputs: `${SYSTEM_PROMPT}\nUser: I have ${ingredientsString}. Please give me a recipe you'd recommend I make!\nAssistant:`,
      parameters: {
        max_new_tokens: 400,
        temperature: 0.7,
      },
    });

    // response.generated_text contains the generated text
    return response.generated_text || "No recipe generated.";
  } catch (error) {
    console.error("Error generating recipe:", error);
    return "Sorry — couldn't generate a recipe right now.";
  }
}