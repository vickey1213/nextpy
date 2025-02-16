## Reference for nextpy/frontend/components/chakra/forms/form(Generated by a LLM. Pending Review)

# Nextpy Forms Documentation

## Form

### Overview

The `form` component in Nextpy is a foundational element used to collect user inputs. It serves as a container for form-related elements like text fields, checkboxes, and buttons.

### Anatomy

The `form` component can include various form controls such as `text_input`, `checkbox`, `radio`, `button`, and custom components.

#### Basic Usage

```python
from nextpy.components.chakra.forms import form

# Create a simple form with an onSubmit event handler
form = form.create(
    TextInput.create(...),
    Button.create("Submit"),
    on_submit=handle_submit
)
```

#### Advanced Usage

```python
from nextpy.components.chakra.forms import Form, form_control, form_label, form_helper_text

# Create an advanced form with form controls and validation
form = form.create(
    form_control.create(
        form_label.create("Email"),
        text_input.create(...),
        form_helper_text.create("Enter a valid email address"),
    ),
    button.create("Submit"),
    on_submit=handle_submit
)
```

### Components

#### Properties

| Prop Name                   | Type                                                       | Description                                                      |
| --------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------- |
| `as_`                       | `str`, `Var[str]`                                          | Specifies the HTML element or custom component the form renders. |
| `reset_on_submit`           | `bool`, `Var[bool]`                                        | If `True`, the form will be reset after submission.              |
| `handle_submit_unique_name` | `str`, `Var[str]`                                          | Unique name for the form's submit handler function.              |
| `style`                     | `Style`                                                    | The style object containing CSS properties.                      |
| `key`                       | `Any`                                                      | A unique key for identifying the component.                      |
| `id`                        | `Any`                                                      | The DOM id attribute of the form.                                |
| `class_name`                | `Any`                                                      | The CSS class name of the form.                                  |
| `autofocus`                 | `bool`                                                     | If `True`, the form will autofocus when loaded.                  |
| `custom_attrs`              | `Dict[str, Union[Var, str]]`                               | Custom attributes for the form element.                          |
| `on_submit`                 | `EventHandler`, `EventSpec`, `list`, `function`, `BaseVar` | Event handler for form submission.                               |

#### Event Triggers

- `on_submit`: Triggered when the form is submitted.

### Notes

- The form component must have a submit button or another element with a type of submit to trigger form submission.
- It is essential to provide an `on_submit` event handler to process the form data.

### Best Practices

- Group related form fields using `FormControl` to provide better structure and accessibility.
- Use `FormLabel` to provide accessible labels for form controls.
- Provide `FormHelperText` to offer additional guidance to the user.
- Utilize `FormErrorMessage` to display validation errors and give immediate feedback to the user.
- Always handle form submission asynchronously to prevent blocking the UI.

## FormControl

### Overview

`FormControl` is a wrapper component that encapsulates a form control with its label and helper text.

### Anatomy

It typically contains a `FormLabel`, an input control (e.g., `TextInput`, `Checkbox`), and optional `FormHelperText` or `FormErrorMessage`.

#### Basic Usage

```python
from nextpy.components.chakra.forms import FormControl, FormLabel, TextInput

# Create a form control with a label and input
form_control = FormControl.create(
    FormLabel.create("Name"),
    TextInput.create(...),
)
```

#### Advanced Usage

```python
from nextpy.components.chakra.forms import FormControl, FormLabel, TextInput, FormHelperText, FormErrorMessage

# Create a form control with label, input, help text, and error message
form_control = FormControl.create(
    FormLabel.create("Name"),
    TextInput.create(...),
    FormHelperText.create("Enter your full name"),
    FormErrorMessage.create("Name is required"),
    is_invalid=True
)
```

### Components

#### Properties

| Prop Name       | Type                                      | Description                                              |
| --------------- | ----------------------------------------- | -------------------------------------------------------- |
| `label`         | `Component`, `str`, `Var[Component, str]` | The label for the form control.                          |
| `input`         | `Component`, `Var[Component]`             | The input control within the form control.               |
| `help_text`     | `Component`, `Var[Component]`             | The helper text providing additional guidance.           |
| `error_message` | `Component`, `Var[Component]`             | The error message displayed when the control is invalid. |
| `is_disabled`   | `bool`, `Var[bool]`                       | If `True`, the form control will be disabled.            |
| `is_invalid`    | `bool`, `Var[bool]`                       | If `True`, the form control is in an error state.        |
| `is_read_only`  | `bool`, `Var[bool]`                       | If `True`, the form control is read-only.                |
| `is_required`   | `bool`, `Var[bool]`                       | If `True`, the form control is required.                 |
| `style`         | `Style`                                   | The style object for the form control.                   |
| `key`           | `Any`                                     | A unique key for the component.                          |
| `id`            | `Any`                                     | The DOM id of the form control.                          |
| `class_name`    | `Any`                                     | The CSS class name of the form control.                  |
| `autofocus`     | `bool`                                    | If `True`, the form control will autofocus when loaded.  |
| `custom_attrs`  | `Dict[str, Union[Var, str]]`              | Custom attributes for the form control element.          |

### Notes

- Ensure that the `label` prop is linked to the input control to maintain accessibility.
- Use `is_invalid` along with `FormErrorMessage` to provide validation feedback.

### Best Practices

- Always provide a `label` for screen readers and accessibility purposes.
- Use `help_text` to guide users on how to fill out the form control.
- Utilize `error_message` to display contextual error messages when validation fails.
- Make use of the `is_required` property to enforce mandatory fields.

## FormLabel, FormHelperText, FormErrorMessage

### Overview

`FormLabel`, `FormHelperText`, and `FormErrorMessage` are utility components used within `FormControl` to build a complete form field with a label, help text, and error messaging.

### Anatomy

These components are typically used within a `FormControl` to label inputs and provide additional context or validation feedback.

#### Basic Usage

```python
from nextpy.components.chakra.forms import FormLabel, FormHelperText, FormErrorMessage

# Create form label, helper text, and error message components
label = FormLabel.create("Email")
helper_text = FormHelperText.create("We will never share your email.")
error_message = FormErrorMessage.create("Email is required.")
```

### Components

#### FormLabel Properties

| Prop Name      | Type                         | Description                                      |
| -------------- | ---------------------------- | ------------------------------------------------ |
| `html_for`     | `str`, `Var[str]`            | Associates the label with a form control by id.  |
| `style`        | `Style`                      | The style object for the label.                  |
| `key`          | `Any`                        | A unique key for the label component.            |
| `id`           | `Any`                        | The DOM id of the label.                         |
| `class_name`   | `Any`                        | The CSS class name of the label.                 |
| `autofocus`    | `bool`                       | If `True`, the label will autofocus when loaded. |
| `custom_attrs` | `Dict[str, Union[Var, str]]` | Custom attributes for the label element.         |

#### FormHelperText & FormErrorMessage Properties

These components share similar properties as `FormLabel`, with the exception of `html_for`.

### Notes

- `FormLabel` should use the `html_for` property to reference the id of the input element it is labeling.
- `FormHelperText` is used to provide additional information about the input.
- `FormErrorMessage` should be shown conditionally, typically when the input has an error.

### Best Practices

- Always use `FormLabel` with the `html_for` attribute for better accessibility.
- `FormHelperText` should be concise and directly related to the input field.
- Only display `FormErrorMessage` when the associated field has a validation error, and make sure the message is clear and helpful.

## Final Considerations

The documentation should provide clear and comprehensive guidance on how to utilize form components effectively within the Nextpy library. It should cover all key properties and behaviors, ensuring that developers have the necessary information to implement forms that are not only functional but also accessible and user-friendly. Each section should be accompanied by code examples that illustrate both basic and advanced use cases, allowing readers to quickly grasp the concepts and apply them to their own projects.
