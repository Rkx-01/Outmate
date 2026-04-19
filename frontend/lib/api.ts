export const getHistory = async () => {
  const response = await fetch('/api/history');
  return response.json();
};

export const getHealth = async () => {
  const response = await fetch('/api/health');
  return response.json();
};

export const getAgents = async () => {
  const response = await fetch('/api/agents');
  return response.json();
};

export const getLogs = async (runId?: string) => {
  const url = runId ? `/api/logs?run_id=${runId}` : '/api/logs';
  const response = await fetch(url);
  return response.json();
};
