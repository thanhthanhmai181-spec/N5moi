/**
 * JLPT N5 December 2021 Practice Test - Application Logic
 * Complete exam simulation with timer, scoring, and result analysis
 */

(function() {
  'use strict';

  // ===== CONFIGURATION =====
  const CONFIG = {
    // JLPT N5 time limits (in seconds)
    sections: {
      vocab: { time: 20 * 60, label: '文字・語彙', labelVi: 'Hán tự - Từ vựng' },
      grammar: { time: 40 * 60, label: '文法・読解', labelVi: 'Ngữ pháp - Đọc hiểu' },
      listening: { time: 30 * 60, label: '聴解', labelVi: 'Nghe hiểu' }
    },
    totalTime: 90 * 60, // 90 minutes total
    // JLPT N5 scoring
    scoring: {
      totalMax: 180,
      passTotal: 85,
      sections: {
        langReading: { max: 120, passMin: 38 }, // 言語知識・読解
        listening: { max: 60, passMin: 19 }       // 聴解
      }
    },
    // Answer keys
    answers: {
      // 文字・語彙 Section
      'vocab-m1-1': '1', 'vocab-m1-2': '4', 'vocab-m1-3': '3',
      'vocab-m1-4': '2', 'vocab-m1-5': '3', 'vocab-m1-6': '1',
      'vocab-m1-7': '2',
      'vocab-m2-8': '3', 'vocab-m2-9': '1', 'vocab-m2-10': '4',
      'vocab-m2-11': '2', 'vocab-m2-12': '3',
      'vocab-m3-13': '2', 'vocab-m3-14': '4', 'vocab-m3-15': '1',
      'vocab-m3-16': '3', 'vocab-m3-17': '1', 'vocab-m3-18': '4',
      'vocab-m4-19': '2', 'vocab-m4-20': '3', 'vocab-m4-21': '4',
      // 文法・読解 Section
      'gram-m1-1': '2', 'gram-m1-2': '4', 'gram-m1-3': '2',
      'gram-m1-4': '2', 'gram-m1-5': '1', 'gram-m1-6': '3',
      'gram-m1-7': '3', 'gram-m1-8': '2', 'gram-m1-9': '4',
      'gram-m2-10': '1', 'gram-m2-11': '1', 'gram-m2-12': '4',
      'gram-m2-13': '4',
      'gram-m3-14': '4', 'gram-m3-15': '3', 'gram-m3-16': '1',
      'gram-m3-17': '1',
      'gram-m4-18': '2', 'gram-m4-19': '2',
      'gram-m5-20': '4', 'gram-m5-21': '3',
      'gram-m6-22': '1',
      // 聴解 Section
      'listen-m1-1': '3', 'listen-m1-2': '4', 'listen-m1-3': '1',
      'listen-m1-4': '4', 'listen-m1-5': '1', 'listen-m1-6': '2',
      'listen-m1-7': '1',
      'listen-m2-1': '2', 'listen-m2-2': '4', 'listen-m2-3': '4',
      'listen-m2-4': '1', 'listen-m2-5': '3', 'listen-m2-6': '4',
      'listen-m3-1': '1', 'listen-m3-2': '2', 'listen-m3-3': '2',
      'listen-m3-4': '3', 'listen-m3-5': '2',
      'listen-m4-1': '3', 'listen-m4-2': '2', 'listen-m4-3': '2',
      'listen-m4-4': '3', 'listen-m4-5': '1', 'listen-m4-6': '3'
    }
  };

  // ===== STATE =====
  let state = {
    studentName: '',
    studentClass: '',
    currentSection: 'vocab',
    timerInterval: null,
    timeRemaining: CONFIG.totalTime,
    examStarted: false,
    examSubmitted: false,
    userAnswers: {}
  };

  // ===== DOM ELEMENTS =====
  const $ = (sel) => document.querySelector(sel);
  const $$ = (sel) => document.querySelectorAll(sel);

  // ===== SCREENS =====
  function showScreen(screenId) {
    $$('.screen').forEach(s => s.classList.remove('active'));
    const screen = $(`#${screenId}`);
    if (screen) {
      screen.classList.add('active');
      window.scrollTo(0, 0);
    }
  }

  // ===== INTRO =====
  function initIntro() {
    const startBtn = $('#btn-start');
    if (!startBtn) return;

    startBtn.addEventListener('click', () => {
      const name = $('#input-name').value.trim();
      const cls = $('#input-class').value.trim();
      
      if (!name) {
        shakeElement($('#input-name'));
        $('#input-name').focus();
        return;
      }
      
      state.studentName = name;
      state.studentClass = cls || 'N/A';
      
      showScreen('screen-exam');
      startExam();
    });

    // Enter key support
    ['#input-name', '#input-class'].forEach(sel => {
      const el = $(sel);
      if (el) {
        el.addEventListener('keypress', (e) => {
          if (e.key === 'Enter') startBtn.click();
        });
      }
    });
  }

  function shakeElement(el) {
    el.style.animation = 'none';
    el.offsetHeight; // reflow
    el.style.animation = 'shake 0.4s ease';
    el.style.borderColor = 'var(--danger)';
    setTimeout(() => {
      el.style.borderColor = '';
      el.style.animation = '';
    }, 1000);
  }

  // ===== EXAM =====
  function startExam() {
    state.examStarted = true;
    state.timeRemaining = CONFIG.totalTime;
    
    // Initialize tab navigation
    initTabs();
    
    // Start timer
    startTimer();
    
    // Initialize answer tracking
    initAnswerTracking();
    
    // Show first section
    switchSection('vocab');
  }

  function initTabs() {
    $$('.tab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const section = btn.dataset.section;
        switchSection(section);
      });
    });
  }

  function switchSection(section) {
    state.currentSection = section;
    
    // Update tabs
    $$('.tab-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.section === section);
    });
    
    // Update panels
    $$('.section-panel').forEach(panel => {
      panel.classList.toggle('active', panel.id === `panel-${section}`);
    });
    
    window.scrollTo(0, 0);
  }

  // ===== TIMER =====
  function startTimer() {
    updateTimerDisplay();
    
    state.timerInterval = setInterval(() => {
      state.timeRemaining--;
      
      if (state.timeRemaining <= 0) {
        state.timeRemaining = 0;
        clearInterval(state.timerInterval);
        autoSubmit();
      }
      
      updateTimerDisplay();
    }, 1000);
  }

  function updateTimerDisplay() {
    const display = $('#timer-display');
    if (!display) return;
    
    const minutes = Math.floor(state.timeRemaining / 60);
    const seconds = state.timeRemaining % 60;
    
    display.textContent = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
    
    // Warning states
    display.classList.remove('warning', 'danger');
    if (state.timeRemaining <= 300) { // 5 minutes
      display.classList.add('danger');
    } else if (state.timeRemaining <= 600) { // 10 minutes
      display.classList.add('warning');
    }
  }

  function autoSubmit() {
    // Auto-submit when time runs out
    if (!state.examSubmitted) {
      showSubmitModal(true);
    }
  }

  // ===== ANSWER TRACKING =====
  function initAnswerTracking() {
    $$('.question-card input[type="radio"]').forEach(input => {
      input.addEventListener('change', (e) => {
        const card = e.target.closest('.question-card');
        const qId = card.dataset.qid;
        const value = e.target.value;
        
        state.userAnswers[qId] = value;
        
        // Update visual selection
        card.querySelectorAll('.option-label').forEach(label => {
          label.classList.remove('selected');
        });
        e.target.closest('.option-label').classList.add('selected');
        
        updateProgress();
      });
    });
  }

  function updateProgress() {
    const totalQuestions = Object.keys(CONFIG.answers).length;
    const answered = Object.keys(state.userAnswers).length;
    const pct = (answered / totalQuestions) * 100;
    
    const bar = $('#progress-fill');
    if (bar) bar.style.width = `${pct}%`;
    
    const text = $('#progress-text');
    if (text) text.textContent = `${answered}/${totalQuestions}`;
  }

  // ===== SUBMIT =====
  function showSubmitModal(timeUp = false) {
    const modal = $('#submit-modal');
    if (!modal) return;
    
    const totalQ = Object.keys(CONFIG.answers).length;
    const answered = Object.keys(state.userAnswers).length;
    const unanswered = totalQ - answered;
    
    const modalTitle = $('#modal-title');
    const modalText = $('#modal-text');
    
    if (timeUp) {
      modalTitle.textContent = '⏰ Hết giờ!';
      modalText.textContent = `Thời gian làm bài đã hết. Bạn đã trả lời ${answered}/${totalQ} câu. Bài thi sẽ được nộp tự động.`;
      // Auto submit after brief delay
      modal.classList.add('show');
      setTimeout(() => {
        submitExam();
      }, 3000);
    } else {
      modalTitle.textContent = '📝 Xác nhận nộp bài';
      if (unanswered > 0) {
        modalText.textContent = `Bạn đã trả lời ${answered}/${totalQ} câu. Còn ${unanswered} câu chưa trả lời. Bạn có chắc muốn nộp bài?`;
      } else {
        modalText.textContent = `Bạn đã trả lời tất cả ${totalQ} câu. Xác nhận nộp bài?`;
      }
      modal.classList.add('show');
    }
  }

  function hideModal() {
    const modal = $('#submit-modal');
    if (modal) modal.classList.remove('show');
  }

  function submitExam() {
    if (state.examSubmitted) return;
    state.examSubmitted = true;
    
    // Stop timer
    clearInterval(state.timerInterval);
    
    // Hide modal
    hideModal();
    
    // Calculate scores
    const results = calculateScores();
    
    // Show results
    showResults(results);
    
    // Mark answers on exam
    markAnswers();
  }

  // ===== SCORING =====
  function calculateScores() {
    const answers = CONFIG.answers;
    const userAnswers = state.userAnswers;
    
    // Count correct by section
    let vocabCorrect = 0, vocabTotal = 0;
    let grammarCorrect = 0, grammarTotal = 0;
    let listeningCorrect = 0, listeningTotal = 0;
    
    for (const [qId, correctAnswer] of Object.entries(answers)) {
      if (qId.startsWith('vocab-')) {
        vocabTotal++;
        if (userAnswers[qId] === correctAnswer) vocabCorrect++;
      } else if (qId.startsWith('gram-')) {
        grammarTotal++;
        if (userAnswers[qId] === correctAnswer) grammarCorrect++;
      } else if (qId.startsWith('listen-')) {
        listeningTotal++;
        if (userAnswers[qId] === correctAnswer) listeningCorrect++;
      }
    }
    
    // Calculate scaled scores (simplified IRT approximation)
    // 言語知識（文字・語彙・文法）・読解: max 120 points
    const langReadingRaw = vocabCorrect + grammarCorrect;
    const langReadingTotal = vocabTotal + grammarTotal;
    const langReadingScore = Math.round((langReadingRaw / langReadingTotal) * 120);
    
    // 聴解: max 60 points  
    const listeningScore = Math.round((listeningCorrect / listeningTotal) * 60);
    
    // Total
    const totalScore = langReadingScore + listeningScore;
    
    // Pass/Fail determination
    const passTotal = totalScore >= CONFIG.scoring.passTotal;
    const passLangReading = langReadingScore >= CONFIG.scoring.sections.langReading.passMin;
    const passListening = listeningScore >= CONFIG.scoring.sections.listening.passMin;
    const passed = passTotal && passLangReading && passListening;
    
    return {
      vocab: { correct: vocabCorrect, total: vocabTotal },
      grammar: { correct: grammarCorrect, total: grammarTotal },
      listening: { correct: listeningCorrect, total: listeningTotal },
      langReadingScore,
      listeningScore,
      totalScore,
      passTotal,
      passLangReading,
      passListening,
      passed
    };
  }

  // ===== RESULTS DISPLAY =====
  function showResults(results) {
    // Update student info
    const nameEl = $('#result-name');
    const classEl = $('#result-class');
    if (nameEl) nameEl.textContent = state.studentName;
    if (classEl) classEl.textContent = state.studentClass;
    
    // Update pass/fail status
    const resultIcon = $('#result-icon');
    const resultTitle = $('#result-title');
    const resultSub = $('#result-sub');
    
    if (results.passed) {
      resultIcon.textContent = '🎉';
      resultTitle.textContent = '合格 - ĐỖ!';
      resultTitle.className = 'pass';
      resultSub.textContent = `Chúc mừng ${state.studentName}! Bạn đã vượt qua kỳ thi JLPT N5.`;
    } else {
      resultIcon.textContent = '📚';
      resultTitle.textContent = '不合格 - CHƯA ĐỖ';
      resultTitle.className = 'fail';
      resultSub.textContent = `Cố gắng thêm nhé ${state.studentName}! Hãy ôn tập lại và thử lại.`;
    }
    
    // Update score cards
    updateScoreCard('score-lang', results.langReadingScore, 120, CONFIG.scoring.sections.langReading.passMin);
    updateScoreCard('score-listening', results.listeningScore, 60, CONFIG.scoring.sections.listening.passMin);
    updateScoreCard('score-total', results.totalScore, 180, CONFIG.scoring.passTotal);
    
    // Update detail table
    const detailBody = $('#detail-tbody');
    if (detailBody) {
      detailBody.innerHTML = `
        <tr>
          <td>文字・語彙 (Từ vựng)</td>
          <td>${results.vocab.correct} / ${results.vocab.total}</td>
          <td>—</td>
          <td>—</td>
        </tr>
        <tr>
          <td>文法・読解 (Ngữ pháp & Đọc hiểu)</td>
          <td>${results.grammar.correct} / ${results.grammar.total}</td>
          <td>—</td>
          <td>—</td>
        </tr>
        <tr>
          <td><strong>言語知識・読解 (Tổng phần 1+2)</strong></td>
          <td><strong>${results.vocab.correct + results.grammar.correct} / ${results.vocab.total + results.grammar.total}</strong></td>
          <td><strong>${results.langReadingScore} / 120</strong></td>
          <td class="${results.passLangReading ? 'status-pass' : 'status-fail'}">${results.passLangReading ? '✅ Đạt (≥38)' : '❌ Chưa đạt (<38)'}</td>
        </tr>
        <tr>
          <td><strong>聴解 (Nghe hiểu)</strong></td>
          <td><strong>${results.listening.correct} / ${results.listening.total}</strong></td>
          <td><strong>${results.listeningScore} / 60</strong></td>
          <td class="${results.passListening ? 'status-pass' : 'status-fail'}">${results.passListening ? '✅ Đạt (≥19)' : '❌ Chưa đạt (<19)'}</td>
        </tr>
        <tr style="border-top: 2px solid var(--primary);">
          <td><strong>Tổng điểm</strong></td>
          <td>—</td>
          <td><strong>${results.totalScore} / 180</strong></td>
          <td class="${results.passTotal ? 'status-pass' : 'status-fail'}">${results.passTotal ? '✅ Đạt (≥85)' : '❌ Chưa đạt (<85)'}</td>
        </tr>
      `;
    }
    
    // Show result screen
    showScreen('screen-result');
  }

  function updateScoreCard(cardId, score, max, passMin) {
    const card = $(`#${cardId}`);
    if (!card) return;
    
    const valueEl = card.querySelector('.score-value');
    const fillEl = card.querySelector('.score-bar-fill');
    
    if (valueEl) {
      // Animate score counting
      animateNumber(valueEl, 0, score, 1500);
    }
    
    if (fillEl) {
      const pct = (score / max) * 100;
      setTimeout(() => {
        fillEl.style.width = `${pct}%`;
      }, 300);
      
      // Color based on performance
      fillEl.classList.remove('good', 'mid', 'low');
      if (score >= passMin * 1.5) {
        fillEl.classList.add('good');
      } else if (score >= passMin) {
        fillEl.classList.add('mid');
      } else {
        fillEl.classList.add('low');
      }
    }
  }

  function animateNumber(el, start, end, duration) {
    const startTime = performance.now();
    
    function update(currentTime) {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
      const current = Math.round(start + (end - start) * eased);
      
      el.textContent = current;
      
      if (progress < 1) {
        requestAnimationFrame(update);
      }
    }
    
    requestAnimationFrame(update);
  }

  // ===== MARK ANSWERS =====
  function markAnswers() {
    const answers = CONFIG.answers;
    
    for (const [qId, correctAnswer] of Object.entries(answers)) {
      const card = $(`.question-card[data-qid="${qId}"]`);
      if (!card) continue;
      
      const userAnswer = state.userAnswers[qId];
      const isCorrect = userAnswer === correctAnswer;
      
      // Mark card
      card.classList.add(isCorrect ? 'correct' : 'incorrect');
      
      // Mark options
      card.querySelectorAll('.option-label').forEach(label => {
        const input = label.querySelector('input[type="radio"]');
        if (!input) return;
        
        if (input.value === correctAnswer) {
          label.classList.add('correct-answer');
        }
        if (input.value === userAnswer && !isCorrect) {
          label.classList.add('wrong-answer');
        }
      });
      
      // Show explanation
      const expEl = card.querySelector('.explanation');
      if (expEl) {
        expEl.classList.add('show');
        expEl.classList.add(isCorrect ? 'correct-exp' : 'incorrect-exp');
        
        if (isCorrect) {
          expEl.innerHTML = `<span class="exp-icon">✅</span> Chính xác!${expEl.dataset.explain ? ' ' + expEl.dataset.explain : ''}`;
        } else {
          const answerText = getAnswerOptionText(card, correctAnswer);
          expEl.innerHTML = `<span class="exp-icon">❌</span> Đáp án đúng: <strong>${correctAnswer}</strong>${answerText ? ` (${answerText})` : ''}${expEl.dataset.explain ? '<br>' + expEl.dataset.explain : ''}`;
        }
      }
    }
  }

  function getAnswerOptionText(card, answerValue) {
    const input = card.querySelector(`input[value="${answerValue}"]`);
    if (!input) return '';
    const label = input.closest('.option-label');
    if (!label) return '';
    const textSpan = label.querySelector('.option-text');
    return textSpan ? textSpan.textContent : '';
  }

  // ===== REVIEW =====
  function reviewAnswers() {
    showScreen('screen-exam');
    // Hide submit bar
    const submitBar = $('#submit-bar');
    if (submitBar) submitBar.style.display = 'none';
  }

  // ===== RETRY =====
  function retryExam() {
    // Reset state
    state.userAnswers = {};
    state.examSubmitted = false;
    state.timeRemaining = CONFIG.totalTime;
    
    // Reset all question cards
    $$('.question-card').forEach(card => {
      card.classList.remove('correct', 'incorrect');
      card.querySelectorAll('.option-label').forEach(label => {
        label.classList.remove('selected', 'correct-answer', 'wrong-answer');
      });
      card.querySelectorAll('input[type="radio"]').forEach(input => {
        input.checked = false;
      });
      const exp = card.querySelector('.explanation');
      if (exp) {
        exp.classList.remove('show', 'correct-exp', 'incorrect-exp');
      }
    });
    
    // Show submit bar again
    const submitBar = $('#submit-bar');
    if (submitBar) submitBar.style.display = '';
    
    // Reset progress
    updateProgress();
    
    // Go back to intro
    showScreen('screen-intro');
  }

  // ===== INITIALIZATION =====
  function init() {
    // Show intro screen
    showScreen('screen-intro');
    
    // Init intro form
    initIntro();
    
    // Submit button
    const submitBtn = $('#btn-submit');
    if (submitBtn) {
      submitBtn.addEventListener('click', () => {
        showSubmitModal(false);
      });
    }
    
    // Modal buttons
    const confirmBtn = $('#modal-confirm');
    if (confirmBtn) {
      confirmBtn.addEventListener('click', submitExam);
    }
    
    const cancelBtn = $('#modal-cancel');
    if (cancelBtn) {
      cancelBtn.addEventListener('click', hideModal);
    }
    
    // Review button
    const reviewBtn = $('#btn-review');
    if (reviewBtn) {
      reviewBtn.addEventListener('click', reviewAnswers);
    }
    
    // Retry button
    const retryBtn = $('#btn-retry');
    if (retryBtn) {
      retryBtn.addEventListener('click', retryExam);
    }
    
    // Back to result button
    const backResultBtn = $('#btn-back-result');
    if (backResultBtn) {
      backResultBtn.addEventListener('click', () => {
        showScreen('screen-result');
      });
    }
    
    // Add CSS shake animation
    const style = document.createElement('style');
    style.textContent = `
      @keyframes shake {
        0%, 100% { transform: translateX(0); }
        25% { transform: translateX(-8px); }
        75% { transform: translateX(8px); }
      }
    `;
    document.head.appendChild(style);
  }

  // Start when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
