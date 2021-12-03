### 前端工程指引

#### 新建配置文件

在`frontend`目录下面新建`local_settings.js`，配置如下内容：

```javascript
module.exports = {
  proxyTableTarget: '线下代理地址',
  devHost: '127.0.0.1'
};
```

### eslint && vetur 检查路径问题

在`根目录`下创建 `vetur.config.js` 文件，配置内容如下：
```javascript
module.exports = {
  projects: [
    './frontend',
    {
      root: './frontend',
      package: './package.json',
      tsconfig: './tsconfig.json',
      snippetFolder: './.vscode/vetur/snippets',
      globalComponents: [
        './src/components/**/*.vue'
      ]
    }
  ]
}
```

#### 运行项目

```shell
// 1. 切换到 /frontend 目录
cd frontend
// 2. 安装 npm 依赖包
npm install
// 3. 更新 magicbox 组件库
npm run dll
// 4. 启动服务
npm run dev 
```
