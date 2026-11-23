# HEIC → PNG 无损批量转换工具

单文件网页应用，双击 `HEIC转PNG-无损批量转换.html` 即可运行。无需安装、无需联网、文件不上传。

## 使用

1. 双击 HTML 文件（Chrome / Edge）。
2. 拖入或选择多个 `.heic` / `.heif` 文件。
3. 点击「开始转换」。
4. 单个下载或「下载全部（ZIP）」。

## 无损实现

- `libheif` WASM 直接解码为 10-bit RGB 数据，写入 **16-bit PNG**（10-bit 值左移 6 位映射到 0–65535），不经 8-bit Canvas。
- 保留 ICC 色彩配置（写入 iCCP chunk）。
- EXIF 拍摄时间 / GPS 导出为同名 `.exif.json`（PNG 无标准 EXIF 容器）。
- HEVC 源压缩本身的有损无法还原；PNG 体积通常为 HEIC 的 3–8 倍。

## 验证结果

| 项 | 结果 |
|---|---|
| file:// 双击运行 | 通过（Edge headless） |
| 16-bit PNG 解码 + 编码 | 通过：1280×854 → 3.2MB PNG，bit depth 16 / color type 6 |
| 像素值映射 | 通过：674 → 43136（正确左移 6 位） |
| 批量 3 文件 | 通过：3/3 成功 |
| ZIP 打包 | 通过：3.2MB PNG → 3.2MB ZIP |
| Blob Worker | file:// 下不可用，已改为主线程逐张处理并让出 UI |

## 重新构建

```bash
cd heic-to-png
python build.py
```

依赖内联在 `vendor/`：`libheif-bundle.js` (1.19.8)、`fflate.js` (0.8.2)。模板在 `src/app.template.html`。
