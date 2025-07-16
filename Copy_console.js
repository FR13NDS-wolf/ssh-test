(() => {
  // 获取文本函数不变
  function getAllTextNodes() {
    let walker = document.createTreeWalker(
      document.body,
      NodeFilter.SHOW_TEXT,
      null,
      false
    );
    let node, texts = [];
    while (node = walker.nextNode()) {
      let txt = node.nodeValue.trim();
      if (txt) texts.push(txt);
    }
    return texts;
  }

  function isChinese(text) {
    return /[\u4e00-\u9fa5]/.test(text);
  }
  function isEnglish(text) {
    return /^[A-Za-z0-9\s.,'"?!\-]+$/.test(text);
  }

  let texts = getAllTextNodes();

  let chineseTexts = texts.filter(t => isChinese(t));
  let englishTexts = texts.filter(t => isEnglish(t));

  let result = '=== 中文内容 ===\n' + chineseTexts.join('\n\n') + '\n\n=== English Content ===\n' + englishTexts.join('\n\n');

  // 创建按钮
  let btn = document.createElement('button');
  btn.textContent = '复制中英文内容到剪贴板';
  btn.style.position = 'fixed';
  btn.style.top = '10px';
  btn.style.right = '10px';
  btn.style.zIndex = 10000;
  btn.style.padding = '10px';
  btn.style.backgroundColor = '#4CAF50';
  btn.style.color = 'white';
  btn.style.border = 'none';
  btn.style.borderRadius = '5px';
  btn.style.cursor = 'pointer';

  btn.onclick = () => {
    navigator.clipboard.writeText(result).then(() => {
      alert('中英文内容已复制到剪切板！');
      btn.remove();
    }).catch(err => {
      alert('复制失败：' + err);
    });
  };

  document.body.appendChild(btn);
})();