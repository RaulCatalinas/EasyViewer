import love from "eslint-config-love"
import pluginReact from "eslint-plugin-react"

export default [
  {
    ...love,
    files: ["**/*.js", "**/*.tsx"],
    rules: {
      "@typescript-eslint/explicit-function-return-type": "off"
    },
    "jsx-runtime": {
      rules: {
        "react/react-in-jsx-scope": "off",
        "react/jsx-uses-react": "off"
      }
    }
  },
  pluginReact.configs.flat.recommended
]
