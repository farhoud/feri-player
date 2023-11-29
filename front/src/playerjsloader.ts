export default new Promise<void>((res) => {
    const script = document.createElement('script');
    script.onload = () => res();
    script.setAttribute(
       'src',
       '/playerjs.js'
    );
    document.head.appendChild(script);
 });