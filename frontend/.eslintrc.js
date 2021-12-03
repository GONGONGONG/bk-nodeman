module.exports = {
  root: true,
  extends: ['plugin:vue/recommended', '@bkui/eslint-config-bk/tsvue'],
  // frontend文件夹不在根目录时, ts会解析错误
  parserOptions: {
    project: 'tsconfig.json',
    tsconfigRootDir: __dirname,
    sourceType: 'module',
  },
  globals: {
    // value 为 true 允许被重写，为 false 不允许被重写
    NODE_ENV: false,
    LOCAL_DEV_URL: false,
    LOCAL_DEV_PORT: false,
    AJAX_URL_PREFIX: false,
    AJAX_MOCK_PARAM: false,
    USER_INFO_URL: false,
    LOGIN_DEV_URL: false,
  },
  rules: {
    '@typescript-eslint/member-ordering': 'off',
    'no-param-reassign': 'off',
  },
};
