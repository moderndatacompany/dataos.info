# COMMENT

## Synopsis

```jsx
COMMENT ON ( TABLE | VIEW | COLUMN ) name IS 'comments'
```

## Description

Set the comment for a object. The comment can be removed by setting the comment to `NULL`.

## Examples

Change the comment for the `users` table to be `master table`:

```jsx
COMMENT ON TABLE users IS 'master table';
```

Change the comment for the `users` view to be `master view`:

```jsx
COMMENT ON VIEW users IS 'master view';
```

Change the comment for the `users.name` column to be `full name`:

```jsx
COMMENT ON COLUMN users.name IS 'full name';
```